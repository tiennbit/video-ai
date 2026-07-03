"""
Unit test THUẦN LOGIC cho tiktok_publish — KHÔNG cần Client Key/Secret, KHÔNG gọi mạng.
Chạy:  cd tiktok_publish && python -m pytest -q
"""
import os
import sys
import time

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config import COVER_TIMESTAMP_MS, SINGLE_CHUNK_MAX  # noqa: E402
from nextcloud_src import build_caption  # noqa: E402
from oauth import _parse_token_response, build_authorize_url, extract_code, pkce_pair  # noqa: E402
from tiktok_api import (build_post_body, chunk_ranges, compute_chunks,  # noqa: E402
                        data_or_raise, validate_privacy)


# ---------- compute_chunks / chunk_ranges ----------
def test_small_file_single_chunk():
    size = 3_500_000  # ~3.5MB (cỡ video thật của kênh)
    chunk, count = compute_chunks(size)
    assert (chunk, count) == (size, 1)


def test_exactly_64mb_single_chunk():
    chunk, count = compute_chunks(SINGLE_CHUNK_MAX)
    assert count == 1 and chunk == SINGLE_CHUNK_MAX


def test_large_file_multi_chunk():
    size = 250 * 1024 * 1024  # 250MB
    chunk, count = compute_chunks(size)
    assert chunk == 10 * 1024 * 1024
    assert count == size // chunk


def test_compute_chunks_rejects_zero():
    with pytest.raises(ValueError):
        compute_chunks(0)


def test_chunk_ranges_cover_whole_file_no_gap():
    size, chunk, count = 250 * 1024 * 1024, 10 * 1024 * 1024, 25
    ranges = chunk_ranges(size, chunk, count)
    assert ranges[0][0] == 0
    assert ranges[-1][1] == size - 1                      # chunk cuối kéo tới hết
    for (s, e), (ns, _ne) in zip(ranges, ranges[1:]):     # liền mạch, không hở
        assert ns == e + 1
    assert sum(e - s + 1 for s, e in ranges) == size      # tổng byte = kích thước file


def test_single_chunk_range():
    size = 3_500_000
    assert chunk_ranges(size, size, 1) == [(0, size - 1)]


# ---------- data_or_raise ----------
def test_data_or_raise_ok():
    payload = {"data": {"publish_id": "v123"}, "error": {"code": "ok", "message": ""}}
    assert data_or_raise(payload)["publish_id"] == "v123"


def test_data_or_raise_error_message():
    payload = {"data": {}, "error": {"code": "invalid_param", "message": "bad title", "log_id": "L1"}}
    with pytest.raises(RuntimeError) as ei:
        data_or_raise(payload)
    assert "invalid_param" in str(ei.value) and "bad title" in str(ei.value)


# ---------- build_post_body: tôn trọng cài đặt tài khoản ----------
def test_body_respects_account_comment_disabled():
    creator = {"comment_disabled": True, "duet_disabled": False, "stitch_disabled": True,
               "privacy_level_options": ["SELF_ONLY"]}
    body = build_post_body("cap #x", "SELF_ONLY", creator, 3_500_000, 3_500_000, 1)
    assert body["post_info"]["privacy_level"] == "SELF_ONLY"
    assert body["post_info"]["disable_comment"] is True    # account tắt -> phải tắt
    assert body["post_info"]["disable_stitch"] is True
    assert body["post_info"]["disable_duet"] is False
    assert body["source_info"] == {"source": "FILE_UPLOAD", "video_size": 3_500_000,
                                   "chunk_size": 3_500_000, "total_chunk_count": 1}


def test_body_cover_points_at_baked_seo_frame():
    """Thumbnail mặc định trỏ vào khung cover SEO nướng ở đầu video (không phải giây 1 như trước)."""
    creator = {"privacy_level_options": ["SELF_ONLY"]}
    body = build_post_body("cap", "SELF_ONLY", creator, 3_500_000, 3_500_000, 1)
    assert body["post_info"]["video_cover_timestamp_ms"] == COVER_TIMESTAMP_MS
    assert COVER_TIMESTAMP_MS < 600  # phải nằm trong khoảng giữ cover tĩnh (~0.6s) của brand.play_cover


# ---------- validate_privacy ----------
def test_validate_privacy_ok():
    validate_privacy("SELF_ONLY", {"privacy_level_options": ["SELF_ONLY", "PUBLIC_TO_EVERYONE"]})


def test_validate_privacy_rejected():
    with pytest.raises(SystemExit):
        validate_privacy("PUBLIC_TO_EVERYONE", {"privacy_level_options": ["SELF_ONLY"]})


# ---------- build_caption ----------
def test_build_caption_joins_and_strips():
    text = "Xáo 1 bộ bài 52 lá — thứ tự chưa ai từng có!\n\n#toan #ly #thpt\n"
    cap = build_caption(text)
    assert cap == "Xáo 1 bộ bài 52 lá — thứ tự chưa ai từng có! #toan #ly #thpt"


def test_build_caption_truncates():
    assert len(build_caption("a" * 5000, max_len=2200)) == 2200


# ---------- oauth token parse ----------
def test_parse_token_response_ok():
    now = int(time.time())
    out = _parse_token_response({
        "access_token": "act", "refresh_token": "rft",
        "expires_in": 86400, "refresh_expires_in": 31536000, "open_id": "oid", "scope": "video.publish",
    })
    assert out["TIKTOK_ACCESS_TOKEN"] == "act"
    assert out["TIKTOK_REFRESH_TOKEN"] == "rft"
    assert int(out["TIKTOK_ACCESS_EXPIRES_AT"]) >= now + 86400 - 2


def test_parse_token_response_error():
    with pytest.raises(RuntimeError):
        _parse_token_response({"error": "invalid_grant", "error_description": "expired code"})


# ---------- PKCE (RFC 7636) ----------
def test_pkce_verifier_length_and_charset():
    import re
    verifier, _ = pkce_pair()
    assert 43 <= len(verifier) <= 128
    assert re.fullmatch(r"[A-Za-z0-9\-._~]+", verifier)  # ký tự hợp lệ RFC 7636


def test_pkce_challenge_is_s256_base64url_nopad():
    import base64
    import hashlib
    verifier, challenge = pkce_pair()
    expect = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    assert challenge == expect
    assert "=" not in challenge and "+" not in challenge and "/" not in challenge  # base64url không padding


def test_pkce_pair_is_random():
    assert pkce_pair()[0] != pkce_pair()[0]


def test_authorize_url_has_pkce_params():
    url = build_authorize_url("ck123", "https://tiennbit.github.io/video-ai/tiktok/callback.html", "st", "CHAL")
    assert "code_challenge=CHAL" in url
    assert "code_challenge_method=S256" in url
    assert "client_key=ck123" in url and "response_type=code" in url


# ---------- extract_code (luồng manual paste) ----------
def test_extract_code_bare():
    assert extract_code("  ABC.123-xyz  ") == ("ABC.123-xyz", None)


def test_extract_code_from_full_url():
    url = "https://tiennbit.github.io/video-ai/tiktok/callback.html?code=XYZ789&state=ST42"
    assert extract_code(url) == ("XYZ789", "ST42")


def test_extract_code_from_query_only():
    assert extract_code("?code=Q1&state=S1") == ("Q1", "S1")


def test_extract_code_error_raises():
    with pytest.raises(SystemExit):
        extract_code("https://x/callback.html?error=access_denied&error_description=nope")
