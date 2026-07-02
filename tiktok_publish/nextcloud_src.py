"""
Nguồn video + caption cho việc đăng TikTok.

- Video: ưu tiên bản render HD LOCAL (media/videos/<slug>_video/1920p60/*.mp4);
  nếu không có, TẢI từ Nextcloud /VideoAI/video/<slug>.mp4 về cache.
- Caption: đọc /VideoAI/thongtin/<slug>.txt trên Nextcloud (fallback noidung/mota/<slug>.txt local).

Tái dùng credential WebDAV ở ~/.config/toanly/nextcloud.env (NGOÀI repo).
"""
from __future__ import annotations

import glob
from pathlib import Path

import requests

from config import NEXTCLOUD_ENV, parse_env

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = REPO_ROOT / "output" / "tiktok_cache"
CAPTION_MAX = 2200  # giới hạn caption TikTok


def _nc() -> dict[str, str]:
    nc = parse_env(NEXTCLOUD_ENV)
    if not nc.get("NC_URL"):
        raise SystemExit(f"Thiếu cấu hình Nextcloud: {NEXTCLOUD_ENV}")
    nc.setdefault("NC_DIR", "VideoAI")
    return nc


def _dav_base(nc: dict[str, str]) -> str:
    return f"{nc['NC_URL']}/remote.php/dav/files/{nc['NC_USER']}/{nc['NC_DIR']}"


def build_caption(text: str, max_len: int = CAPTION_MAX) -> str:
    """Ghép nội dung file thông tin thành 1 caption TikTok (gộp dòng, bỏ dòng trống)."""
    parts = [ln.strip() for ln in (text or "").splitlines() if ln.strip()]
    caption = " ".join(parts).strip()
    return caption[:max_len]


def local_video(slug: str) -> Path | None:
    """Đường dẫn MP4 HD local (nếu đã render). None nếu chưa có."""
    hits = glob.glob(str(REPO_ROOT / "media" / "videos" / f"{slug}_video" / "1920p60" / "*.mp4"))
    hits = [h for h in hits if "partial" not in h]
    return Path(hits[0]) if hits else None


def read_caption(slug: str) -> str:
    """Caption từ Nextcloud /thongtin/<slug>.txt; fallback noidung/mota/<slug>.txt local."""
    nc = _nc()
    url = f"{_dav_base(nc)}/thongtin/{slug}.txt"
    try:
        r = requests.get(url, auth=(nc["NC_USER"], nc["NC_PASS"]), timeout=30)
        if r.status_code == 200 and r.text.strip():
            return build_caption(r.text)
    except requests.RequestException:
        pass
    local = REPO_ROOT / "noidung" / "mota" / f"{slug}.txt"
    if local.exists():
        return build_caption(local.read_text(encoding="utf-8"))
    return slug  # không có caption -> dùng slug tạm


def fetch_video(slug: str) -> Path:
    """Trả path MP4 để upload: local nếu có, không thì tải từ Nextcloud về cache."""
    lv = local_video(slug)
    if lv:
        return lv
    nc = _nc()
    url = f"{_dav_base(nc)}/video/{slug}.mp4"
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    dest = CACHE_DIR / f"{slug}.mp4"
    with requests.get(url, auth=(nc["NC_USER"], nc["NC_PASS"]), stream=True, timeout=120) as r:
        if r.status_code != 200:
            raise SystemExit(f"Không tải được video từ Nextcloud ({r.status_code}): {url}")
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 512):
                if chunk:
                    f.write(chunk)
    return dest


def list_published_slugs() -> list[str]:
    """Danh sách slug đang có trên Nextcloud /VideoAI/video/ (nguồn cho chế độ hàng đợi)."""
    nc = _nc()
    r = requests.request(
        "PROPFIND", f"{_dav_base(nc)}/video/",
        auth=(nc["NC_USER"], nc["NC_PASS"]), headers={"Depth": "1"}, timeout=30,
    )
    if r.status_code not in (207, 200):
        raise SystemExit(f"PROPFIND /video/ lỗi ({r.status_code})")
    import re
    slugs = re.findall(r"/video/([^/<]+)\.mp4", r.text)
    return sorted(set(slugs))
