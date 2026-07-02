"""
Cấu hình + kho token cho TikTok Content Posting API.

MỌI BÍ MẬT nằm NGOÀI repo, tại ~/.config/toanly/tiktok.env (không commit).
File đó chứa (KEY=VALUE mỗi dòng):
    TIKTOK_CLIENT_KEY=...        # bắt buộc — điền sau khi tạo app
    TIKTOK_CLIENT_SECRET=...     # bắt buộc
    TIKTOK_REDIRECT_URI=http://localhost:8723/callback   # phải KHỚP app
    TIKTOK_PRIVACY_LEVEL=SELF_ONLY   # hook đổi PUBLIC_TO_EVERYONE sau khi audit
    # --- các dòng dưới do script tự ghi sau khi login, KHÔNG cần điền tay ---
    TIKTOK_ACCESS_TOKEN=...
    TIKTOK_REFRESH_TOKEN=...
    TIKTOK_ACCESS_EXPIRES_AT=...     # epoch giây
    TIKTOK_REFRESH_EXPIRES_AT=...
    TIKTOK_OPEN_ID=...
"""
from __future__ import annotations

import os
from pathlib import Path

# ---- Endpoint chính thức (developers.tiktok.com, API v2) ----
AUTH_URL = "https://www.tiktok.com/v2/auth/authorize/"
TOKEN_URL = "https://open.tiktokapis.com/v2/oauth/token/"
CREATOR_INFO_URL = "https://open.tiktokapis.com/v2/post/publish/creator_info/query/"
VIDEO_INIT_URL = "https://open.tiktokapis.com/v2/post/publish/video/init/"
STATUS_URL = "https://open.tiktokapis.com/v2/post/publish/status/fetch/"

# Scope cần cho ĐĂNG TRỰC TIẾP (direct post). Nếu chỉ upload nháp vào hộp thư -> "video.upload".
SCOPES = "user.info.basic,video.publish"

# Giới hạn chunk theo tài liệu FILE_UPLOAD: 5MB..64MB; file nhỏ đăng 1 chunk.
CHUNK_MIN = 5 * 1024 * 1024
CHUNK_MAX = 64 * 1024 * 1024
SINGLE_CHUNK_MAX = 64 * 1024 * 1024  # <= mức này -> đăng 1 chunk (chunk_size = cả file)

# TikTok KHÔNG hỗ trợ redirect localhost -> dùng trang tĩnh HTTPS công khai (GitHub Pages).
DEFAULT_REDIRECT_URI = "https://tiennbit.github.io/video-ai/tiktok/callback.html"
DEFAULT_PRIVACY = "SELF_ONLY"  # app CHƯA audit chỉ được SELF_ONLY

TIKTOK_ENV = Path(os.path.expanduser("~/.config/toanly/tiktok.env"))
NEXTCLOUD_ENV = Path(os.path.expanduser("~/.config/toanly/nextcloud.env"))
# Log các slug ĐÃ đăng TikTok (ngoài repo) — chống đăng trùng.
POSTED_LOG = Path(os.path.expanduser("~/.config/toanly/tiktok_posted.log"))
# Lưu tạm PKCE verifier + state giữa bước login (mở URL) và bước auth (dán code).
PKCE_STATE = Path(os.path.expanduser("~/.config/toanly/.tiktok_pkce.json"))


def parse_env(path: Path) -> dict[str, str]:
    """Đọc file KEY=VALUE (bỏ dòng trống/comment). Trả {} nếu không có file."""
    out: dict[str, str] = {}
    if not path.exists():
        return out
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip()
    return out


def load_config() -> dict[str, str]:
    """Nạp tiktok.env; áp mặc định cho redirect/privacy nếu thiếu."""
    cfg = parse_env(TIKTOK_ENV)
    cfg.setdefault("TIKTOK_REDIRECT_URI", DEFAULT_REDIRECT_URI)
    cfg.setdefault("TIKTOK_PRIVACY_LEVEL", DEFAULT_PRIVACY)
    return cfg


def save_tokens(updates: dict[str, str]) -> None:
    """Ghi/đè các KEY token vào tiktok.env, GIỮ nguyên các key khác. Tạo file nếu chưa có."""
    TIKTOK_ENV.parent.mkdir(parents=True, exist_ok=True)
    existing = parse_env(TIKTOK_ENV)
    existing.update({k: str(v) for k, v in updates.items()})
    lines = [f"{k}={v}" for k, v in existing.items()]
    TIKTOK_ENV.write_text("\n".join(lines) + "\n", encoding="utf-8")
    try:
        os.chmod(TIKTOK_ENV, 0o600)
    except OSError:
        pass


def require(cfg: dict[str, str], *keys: str) -> None:
    """Báo lỗi rõ ràng nếu thiếu key bắt buộc (vd chưa điền Client Key)."""
    missing = [k for k in keys if not cfg.get(k)]
    if missing:
        raise SystemExit(
            "Thiếu cấu hình bắt buộc trong "
            f"{TIKTOK_ENV}: {', '.join(missing)}.\n"
            "Xem tiktok_publish/SETUP.md để biết cách tạo app + điền Client Key/Secret."
        )
