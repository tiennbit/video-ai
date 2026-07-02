#!/usr/bin/env python3
"""
CLI đăng TikTok qua Content Posting API (đăng trực tiếp, mặc định SELF_ONLY).

Dùng:
    python tiktok_publish/publish.py login          # lần đầu: lấy token OAuth
    python tiktok_publish/publish.py <slug>         # đăng 1 tập (vd: gps)
    python tiktok_publish/publish.py --queue        # đăng mọi video trên Nextcloud chưa đăng TikTok
    python tiktok_publish/publish.py --list         # xem tình trạng (đã có / đã đăng)

Đổi sang PUBLIC sau khi app qua audit: sửa TIKTOK_PRIVACY_LEVEL=PUBLIC_TO_EVERYONE trong tiktok.env.
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# In tiếng Việt an toàn trên console Windows (cp1252) — ép UTF-8, không crash.
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
    except Exception:  # noqa: BLE001
        pass

from config import DEFAULT_PRIVACY, POSTED_LOG, load_config  # noqa: E402
from nextcloud_src import fetch_video, list_published_slugs, read_caption  # noqa: E402
from oauth import login as oauth_login  # noqa: E402
from oauth import valid_access_token  # noqa: E402
from tiktok_api import (build_post_body, compute_chunks, init_video, poll_status,  # noqa: E402
                        query_creator_info, upload_file, validate_privacy)


def _posted_slugs() -> set[str]:
    if not POSTED_LOG.exists():
        return set()
    out = set()
    for line in POSTED_LOG.read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if len(parts) >= 2:
            out.add(parts[1])
    return out


def mark_posted(slug: str, publish_id: str) -> None:
    POSTED_LOG.parent.mkdir(parents=True, exist_ok=True)
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(POSTED_LOG, "a", encoding="utf-8") as f:
        f.write(f"{ts} {slug} {publish_id}\n")


def publish_one(slug: str, cfg: dict | None = None) -> str:
    cfg = cfg or load_config()
    privacy = cfg.get("TIKTOK_PRIVACY_LEVEL", DEFAULT_PRIVACY)
    token = valid_access_token(cfg)

    caption = read_caption(slug)
    video = fetch_video(slug)
    size = Path(video).stat().st_size
    print(f"→ {slug}: video={video} ({size/1e6:.1f} MB), caption='{caption[:60]}…', privacy={privacy}")

    creator = query_creator_info(token)
    validate_privacy(privacy, creator)
    chunk_size, count = compute_chunks(size)
    body = build_post_body(caption, privacy, creator, size, chunk_size, count)

    init = init_video(token, body)
    publish_id, upload_url = init["publish_id"], init["upload_url"]
    print(f"  init OK · publish_id={publish_id} · upload {count} chunk")
    upload_file(upload_url, str(video), size, chunk_size, count)
    status = poll_status(token, publish_id)
    mark_posted(slug, publish_id)
    print(f"✓ ĐÃ ĐĂNG TikTok: {slug} · status={status.get('status')} · privacy={privacy}")
    return publish_id


def run_queue() -> int:
    posted = _posted_slugs()
    todo = [s for s in list_published_slugs() if s not in posted]
    if not todo:
        print("Không có video mới cần đăng TikTok (tất cả đã đăng).")
        return 0
    print(f"Sẽ đăng {len(todo)} tập: {', '.join(todo)}")
    n_ok = n_fail = 0
    for slug in todo:
        try:
            publish_one(slug)
            n_ok += 1
        except Exception as e:  # noqa: BLE001 — 1 tập lỗi không chặn cả hàng đợi
            n_fail += 1
            print(f"✗ LỖI đăng {slug}: {e}", file=sys.stderr)
    print(f"== Xong: {n_ok} đăng, {n_fail} lỗi ==")
    return 1 if n_fail else 0


def show_list() -> None:
    posted = _posted_slugs()
    pub = list_published_slugs()
    print(f"Trên Nextcloud /VideoAI/video: {len(pub)} video")
    for s in pub:
        print(f"  {'✓ đã đăng TikTok' if s in posted else '· chưa đăng   '}  {s}")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Đăng TikTok qua Content Posting API (SELF_ONLY mặc định).")
    ap.add_argument("slug", nargs="?", help="slug tập cần đăng (vd: gps). Bỏ trống nếu dùng cờ.")
    ap.add_argument("--queue", action="store_true", help="đăng mọi video Nextcloud chưa đăng TikTok")
    ap.add_argument("--list", action="store_true", help="liệt kê tình trạng đăng")
    args = ap.parse_args(argv)

    if args.slug == "login":
        oauth_login()
        return 0
    if args.list:
        show_list()
        return 0
    if args.queue:
        return run_queue()
    if args.slug:
        try:
            publish_one(args.slug)
            return 0
        except Exception as e:  # noqa: BLE001
            print(f"✗ LỖI: {e}", file=sys.stderr)
            return 1
    ap.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
