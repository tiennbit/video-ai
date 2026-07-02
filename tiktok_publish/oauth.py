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

import secrets
import time
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests

from config import AUTH_URL, SCOPES, TOKEN_URL, load_config, require, save_tokens


def build_authorize_url(client_key: str, redirect_uri: str, state: str, scopes: str = SCOPES) -> str:
    params = {
        "client_key": client_key,
        "scope": scopes,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "state": state,
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


def exchange_code(cfg: dict, code: str) -> dict[str, str]:
    payload = _post_token({
        "client_key": cfg["TIKTOK_CLIENT_KEY"],
        "client_secret": cfg["TIKTOK_CLIENT_SECRET"],
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": cfg["TIKTOK_REDIRECT_URI"],
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


# ---- local callback server ----
class _Handler(BaseHTTPRequestHandler):
    server_version = "TikTokLoginHelper/1.0"

    def do_GET(self):  # noqa: N802
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path.rstrip("/") not in ("/callback", ""):
            self.send_response(404); self.end_headers(); return
        qs = urllib.parse.parse_qs(parsed.query)
        self.server.oauth_result = {  # type: ignore[attr-defined]
            "code": qs.get("code", [None])[0],
            "state": qs.get("state", [None])[0],
            "error": qs.get("error", [None])[0],
        }
        body = "<h2>Đã nhận phản hồi TikTok. Bạn có thể đóng tab này.</h2>"
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def log_message(self, *args):  # tắt log ồn
        pass


def login(open_browser: bool = True) -> dict[str, str]:
    """Chạy luồng login đầy đủ; trả token đã lưu."""
    cfg = load_config()
    require(cfg, "TIKTOK_CLIENT_KEY", "TIKTOK_CLIENT_SECRET")
    redirect = cfg["TIKTOK_REDIRECT_URI"]
    parsed = urllib.parse.urlparse(redirect)
    host, port = parsed.hostname or "localhost", parsed.port or 80
    state = secrets.token_urlsafe(16)

    url = build_authorize_url(cfg["TIKTOK_CLIENT_KEY"], redirect, state)
    print("Mở trình duyệt để đăng nhập TikTok...\nNếu không tự mở, dán URL sau vào trình duyệt:\n" + url)
    if open_browser:
        webbrowser.open(url)

    httpd = HTTPServer((host, port), _Handler)
    httpd.oauth_result = None  # type: ignore[attr-defined]
    print(f"Đang chờ callback tại {redirect} ...")
    while httpd.oauth_result is None:  # type: ignore[attr-defined]
        httpd.handle_request()
    res = httpd.oauth_result  # type: ignore[attr-defined]

    if res.get("error"):
        raise SystemExit(f"TikTok từ chối cấp quyền: {res['error']}")
    if res.get("state") != state:
        raise SystemExit("State không khớp — nghi ngờ CSRF, huỷ.")
    if not res.get("code"):
        raise SystemExit("Không nhận được authorization code.")

    tokens = exchange_code(cfg, res["code"])
    print(f"Đăng nhập OK. open_id={tokens.get('TIKTOK_OPEN_ID','')[:10]}… Token đã lưu vào {config_env()}.")
    return tokens


def config_env():
    from config import TIKTOK_ENV
    return TIKTOK_ENV
