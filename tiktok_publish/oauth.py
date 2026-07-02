"""
OAuth 2.0 cho TikTok (authorization code flow, client bí mật).

Luồng login cá nhân:
  1) mở trình duyệt tới AUTH_URL (kèm client_key, scope, redirect_uri, state)
  2) chạy 1 local HTTP server bắt callback ?code=...&state=...
  3) đổi code -> access_token + refresh_token (POST TOKEN_URL)
  4) lưu token vào ~/.config/toanly/tiktok.env

Tự refresh access_token khi hết hạn (dùng refresh_token).
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import secrets
import time
import urllib.parse
import webbrowser

import requests

from config import (AUTH_URL, PKCE_STATE, SCOPES, TIKTOK_ENV, TOKEN_URL,
                    load_config, require, save_tokens)


def pkce_pair() -> tuple[str, str]:
    """(code_verifier, code_challenge) theo RFC 7636, method S256.
    - verifier: 43–128 ký tự trong [A-Za-z0-9-._~] (token_urlsafe dùng [A-Za-z0-9-_], là tập con hợp lệ).
    - challenge = base64url( SHA256(verifier) ) KHÔNG padding.
    THUẦN LOGIC (test được)."""
    verifier = secrets.token_urlsafe(64)  # ~86 ký tự
    digest = hashlib.sha256(verifier.encode("ascii")).digest()
    challenge = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
    return verifier, challenge


def build_authorize_url(client_key: str, redirect_uri: str, state: str,
                        code_challenge: str, scopes: str = SCOPES) -> str:
    params = {
        "client_key": client_key,
        "scope": scopes,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "state": state,
        "code_challenge": code_challenge,     # PKCE — TikTok Login Kit yêu cầu
        "code_challenge_method": "S256",
    }
    return AUTH_URL + "?" + urllib.parse.urlencode(params)


def _parse_token_response(payload: dict) -> dict[str, str]:
    """Chuyển JSON token (phẳng, API v2) -> dict để lưu env. Ném lỗi nếu API báo error.
    THUẦN LOGIC (test được, không cần mạng)."""
    # v2 trả lỗi ở "error"/"error_description" (chuỗi) khi thất bại.
    err = payload.get("error")
    if err and err not in ("", "ok"):
        desc = payload.get("error_description") or payload.get("log_id") or ""
        raise RuntimeError(f"TikTok OAuth lỗi: {err} — {desc}")
    if "access_token" not in payload:
        raise RuntimeError(f"Phản hồi token không hợp lệ: {payload}")
    now = int(time.time())
    return {
        "TIKTOK_ACCESS_TOKEN": payload["access_token"],
        "TIKTOK_REFRESH_TOKEN": payload.get("refresh_token", ""),
        "TIKTOK_ACCESS_EXPIRES_AT": str(now + int(payload.get("expires_in", 0))),
        "TIKTOK_REFRESH_EXPIRES_AT": str(now + int(payload.get("refresh_expires_in", 0))),
        "TIKTOK_OPEN_ID": payload.get("open_id", ""),
        "TIKTOK_SCOPE": payload.get("scope", ""),
    }


def _post_token(data: dict) -> dict:
    r = requests.post(
        TOKEN_URL, data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded", "Cache-Control": "no-cache"},
        timeout=30,
    )
    try:
        return r.json()
    except ValueError:
        raise RuntimeError(f"Token endpoint trả về không phải JSON (HTTP {r.status_code}): {r.text[:300]}")


def exchange_code(cfg: dict, code: str, code_verifier: str) -> dict[str, str]:
    payload = _post_token({
        "client_key": cfg["TIKTOK_CLIENT_KEY"],
        "client_secret": cfg["TIKTOK_CLIENT_SECRET"],
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": cfg["TIKTOK_REDIRECT_URI"],
        "code_verifier": code_verifier,       # PKCE — khớp code_challenge đã gửi ở authorize
    })
    tokens = _parse_token_response(payload)
    save_tokens(tokens)
    return tokens


def refresh(cfg: dict) -> dict[str, str]:
    if not cfg.get("TIKTOK_REFRESH_TOKEN"):
        raise SystemExit("Chưa có refresh_token — hãy chạy: python tiktok_publish/publish.py login")
    payload = _post_token({
        "client_key": cfg["TIKTOK_CLIENT_KEY"],
        "client_secret": cfg["TIKTOK_CLIENT_SECRET"],
        "grant_type": "refresh_token",
        "refresh_token": cfg["TIKTOK_REFRESH_TOKEN"],
    })
    tokens = _parse_token_response(payload)
    save_tokens(tokens)
    return tokens


def valid_access_token(cfg: dict | None = None, skew: int = 120) -> str:
    """Trả access_token còn hạn; tự refresh nếu sắp/đã hết hạn (đệm `skew` giây)."""
    cfg = cfg or load_config()
    require(cfg, "TIKTOK_CLIENT_KEY", "TIKTOK_CLIENT_SECRET")
    exp = int(cfg.get("TIKTOK_ACCESS_EXPIRES_AT", "0") or "0")
    if not cfg.get("TIKTOK_ACCESS_TOKEN") or int(time.time()) >= exp - skew:
        cfg = {**cfg, **refresh(cfg)}
    return cfg["TIKTOK_ACCESS_TOKEN"]


# ---- luồng MANUAL (redirect HTTPS công khai; KHÔNG local server) ----
def extract_code(text: str) -> tuple[str, str | None]:
    """Từ chuỗi user dán (code trần HOẶC nguyên URL redirect) -> (code, state|None).
    Nếu URL có 'error' thì raise. THUẦN LOGIC (test được)."""
    text = (text or "").strip()
    if text.startswith("http") or "code=" in text or "error=" in text:
        q = urllib.parse.urlparse(text).query or text.split("?", 1)[-1]
        params = dict(urllib.parse.parse_qsl(q))
        if params.get("error"):
            raise SystemExit(f"TikTok trả về lỗi: {params['error']} — {params.get('error_description', '')}")
        code = params.get("code", "")
        if not code:
            raise SystemExit(f"Không tìm thấy 'code' trong chuỗi đã dán: {text[:80]}")
        return code, params.get("state")
    return text, None


def _save_pkce(verifier: str, state: str, redirect_uri: str) -> None:
    PKCE_STATE.parent.mkdir(parents=True, exist_ok=True)
    PKCE_STATE.write_text(
        json.dumps({"verifier": verifier, "state": state, "redirect_uri": redirect_uri}),
        encoding="utf-8",
    )
    try:
        os.chmod(PKCE_STATE, 0o600)
    except OSError:
        pass


def _load_pkce() -> dict:
    if not PKCE_STATE.exists():
        raise SystemExit("Chưa có phiên login đang chờ. Hãy chạy trước: python tiktok_publish/publish.py login")
    return json.loads(PKCE_STATE.read_text(encoding="utf-8"))


def login_start(open_browser: bool = True) -> str:
    """BƯỚC 1: sinh PKCE + state, LƯU TẠM ra file, in authorize URL, mở trình duyệt. Trả URL."""
    cfg = load_config()
    require(cfg, "TIKTOK_CLIENT_KEY", "TIKTOK_CLIENT_SECRET")
    redirect = cfg["TIKTOK_REDIRECT_URI"]
    state = secrets.token_urlsafe(16)
    verifier, challenge = pkce_pair()
    _save_pkce(verifier, state, redirect)
    url = build_authorize_url(cfg["TIKTOK_CLIENT_KEY"], redirect, state, challenge)
    print("=== BƯỚC 1/2: CẤP QUYỀN TIKTOK ===")
    print("Mở URL sau trong trình duyệt (đã thử tự mở):\n")
    print(url + "\n")
    print(f"Sau khi bấm Authorize, trang callback ({redirect})")
    print("sẽ hiện 'code'. Copy code (hoặc cả URL) rồi chạy BƯỚC 2:\n")
    print('    python tiktok_publish/publish.py auth "<dán code hoặc URL>"\n')
    if open_browser:
        try:
            webbrowser.open(url)
        except Exception:  # noqa: BLE001
            pass
    return url


def login_finish(code_or_url: str) -> dict[str, str]:
    """BƯỚC 2: đọc verifier+state đã lưu, trích code, verify state, đổi token."""
    saved = _load_pkce()
    cfg = load_config()
    code, state = extract_code(code_or_url)
    if state is not None and state != saved.get("state"):
        raise SystemExit("State không khớp — nghi ngờ CSRF, huỷ. Chạy lại 'login'.")
    tokens = exchange_code(cfg, code, saved["verifier"])
    try:
        PKCE_STATE.unlink()
    except OSError:
        pass
    print(f"Đăng nhập OK. open_id={tokens.get('TIKTOK_OPEN_ID', '')[:10]}… Token đã lưu vào {TIKTOK_ENV}.")
    return tokens
