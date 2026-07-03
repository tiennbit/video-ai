"""
Client TikTok Content Posting API (v2) — ĐĂNG TRỰC TIẾP (direct post).

Luồng chuẩn:
  creator_info/query  -> lấy quyền (privacy options, comment/duet/stitch, thời lượng max)
  video/init          -> gửi post_info + source_info(FILE_UPLOAD) -> nhận publish_id + upload_url
  PUT upload_url      -> tải file theo Content-Range (chia khúc nếu > 64MB)
  status/fetch        -> poll tới PUBLISH_COMPLETE / FAILED

CHỈ dùng API chính thức (Bearer token). Không browser automation, không giả chữ ký.
"""
from __future__ import annotations

import math
import time

import requests

from config import (COVER_TIMESTAMP_MS, CREATOR_INFO_URL, SINGLE_CHUNK_MAX, STATUS_URL, VIDEO_INIT_URL)

JSON_HEADERS = {"Content-Type": "application/json; charset=UTF-8"}
DEFAULT_CHUNK = 10 * 1024 * 1024  # 10MB cho file lớn


# ---------------- THUẦN LOGIC (test được, không cần mạng) ----------------
def data_or_raise(payload: dict) -> dict:
    """Trả payload['data']; ném RuntimeError với message TikTok nếu error.code != 'ok'."""
    err = payload.get("error") or {}
    code = err.get("code", "ok")
    if code and code != "ok":
        raise RuntimeError(
            f"TikTok API lỗi [{code}]: {err.get('message', '')} (log_id={err.get('log_id', '')})"
        )
    return payload.get("data", {})


def compute_chunks(video_size: int) -> tuple[int, int]:
    """(chunk_size, total_chunk_count). File <= 64MB -> 1 chunk = cả file."""
    if video_size <= 0:
        raise ValueError("video_size phải > 0")
    if video_size <= SINGLE_CHUNK_MAX:
        return video_size, 1
    chunk = DEFAULT_CHUNK
    count = max(1, video_size // chunk)  # chunk cuối ôm phần dư
    return chunk, count


def chunk_ranges(video_size: int, chunk_size: int, count: int) -> list[tuple[int, int]]:
    """Danh sách (start, end) cho từng chunk; chunk cuối kéo tới hết file."""
    ranges = []
    for i in range(count):
        start = i * chunk_size
        end = video_size - 1 if i == count - 1 else start + chunk_size - 1
        ranges.append((start, end))
    return ranges


def build_post_body(caption: str, privacy: str, creator_info: dict,
                    video_size: int, chunk_size: int, count: int,
                    cover_ms: int = COVER_TIMESTAMP_MS) -> dict:
    """Dựng body cho video/init. Tôn trọng cài đặt tài khoản (comment/duet/stitch bị tắt thì phải để tắt).
    cover_ms: mốc khung hình dùng làm thumbnail (mặc định trỏ vào khung cover SEO nướng ở đầu video)."""
    return {
        "post_info": {
            "title": caption,
            "privacy_level": privacy,
            # TikTok BẮT BUỘC theo cài đặt tài khoản: nếu account tắt thì không bật được.
            "disable_comment": bool(creator_info.get("comment_disabled", False)),
            "disable_duet": bool(creator_info.get("duet_disabled", False)),
            "disable_stitch": bool(creator_info.get("stitch_disabled", False)),
            "video_cover_timestamp_ms": cover_ms,
        },
        "source_info": {
            "source": "FILE_UPLOAD",
            "video_size": video_size,
            "chunk_size": chunk_size,
            "total_chunk_count": count,
        },
    }


def validate_privacy(privacy: str, creator_info: dict) -> None:
    opts = creator_info.get("privacy_level_options") or []
    if opts and privacy not in opts:
        raise SystemExit(
            f"privacy_level '{privacy}' không nằm trong quyền cho phép {opts}. "
            "App CHƯA audit thường chỉ có SELF_ONLY. Sửa TIKTOK_PRIVACY_LEVEL trong tiktok.env."
        )


# ---------------- GỌI MẠNG ----------------
def _bearer(token: str) -> dict:
    return {"Authorization": f"Bearer {token}"}


def query_creator_info(access_token: str) -> dict:
    r = requests.post(CREATOR_INFO_URL, headers={**_bearer(access_token), **JSON_HEADERS}, json={}, timeout=30)
    return data_or_raise(r.json())


def init_video(access_token: str, body: dict) -> dict:
    r = requests.post(VIDEO_INIT_URL, headers={**_bearer(access_token), **JSON_HEADERS}, json=body, timeout=60)
    return data_or_raise(r.json())  # {publish_id, upload_url}


def upload_file(upload_url: str, file_path: str, video_size: int, chunk_size: int, count: int) -> None:
    """PUT từng chunk lên upload_url theo Content-Range."""
    with open(file_path, "rb") as f:
        for (start, end) in chunk_ranges(video_size, chunk_size, count):
            f.seek(start)
            blob = f.read(end - start + 1)
            headers = {
                "Content-Type": "video/mp4",
                "Content-Range": f"bytes {start}-{end}/{video_size}",
                "Content-Length": str(len(blob)),
            }
            resp = requests.put(upload_url, headers=headers, data=blob, timeout=300)
            if resp.status_code not in (200, 201, 206):
                raise RuntimeError(f"Upload chunk {start}-{end} thất bại (HTTP {resp.status_code}): {resp.text[:300]}")


def poll_status(access_token: str, publish_id: str, interval: float = 3.0, timeout: float = 300.0) -> dict:
    """Poll tới khi PUBLISH_COMPLETE hoặc FAILED (hoặc SEND_TO_USER_INBOX với luồng upload)."""
    deadline = time.time() + timeout
    last = {}
    while time.time() < deadline:
        r = requests.post(STATUS_URL, headers={**_bearer(access_token), **JSON_HEADERS},
                          json={"publish_id": publish_id}, timeout=30)
        last = data_or_raise(r.json())
        status = last.get("status")
        if status in ("PUBLISH_COMPLETE", "SEND_TO_USER_INBOX"):
            return last
        if status == "FAILED":
            reason = last.get("fail_reason") or last.get("failReason") or last
            raise RuntimeError(f"TikTok đăng THẤT BẠI: {reason}")
        time.sleep(interval)
    raise RuntimeError(f"Hết thời gian chờ status (publish_id={publish_id}); trạng thái cuối: {last}")
