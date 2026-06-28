#!/usr/bin/env python3
# =============================================================================
# Tạo (seed) file THÔNG TIN cho 1 tập video: noidung/mota/<slug>.txt
#
# Format (CHỈ 2 phần):
#   <Title SEO TikTok — gợi tò mò>
#   <dòng trống>
#   #toan #ly #thpt #hsa #tsa
#
# Cách sinh title (lúc render KHÔNG có Claude/API):
#   - Lấy câu HỎI gợi tò mò có sẵn trong lời thoại hook (câu kết thúc bằng '?').
#   - Không có '?' -> lấy câu đầu của hook.
#   - Không có lời thoại -> fallback TITLES (app_backend) hoặc slug.
#   File ĐÃ CÓ -> GIỮ NGUYÊN (tôn trọng bản người dùng đã tinh chỉnh).
#
# Dùng:
#   python scenes/make_description.py <slug>
#
# Chỉ dùng thư viện chuẩn (stdlib). Dòng cuối stdout LUÔN là path file (shell đọc).
# =============================================================================
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCENES = ROOT / "scenes"
MOTA_DIR = ROOT / "noidung" / "mota"

# Hashtag CỐ ĐỊNH (theo yêu cầu) — sửa tại đây nếu đổi định hướng kênh.
FIXED_HASHTAGS = "#toan #ly #thpt #hsa #tsa"


def _load_segments(slug: str) -> dict:
    """Nạp SEGMENTS từ scenes/narration_texts_<slug>.py (hoặc narration_<slug>.py).
    Trả {} nếu không tìm thấy / lỗi import."""
    for name in (f"narration_texts_{slug}.py", f"narration_{slug}.py"):
        path = SCENES / name
        if not path.exists():
            continue
        try:
            spec = importlib.util.spec_from_file_location(f"_narr_{slug}", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)  # type: ignore[union-attr]
            seg = getattr(mod, "SEGMENTS", None)
            if isinstance(seg, dict):
                return seg
        except Exception as e:  # noqa: BLE001 — seed là tùy chọn, không làm vỡ pipeline
            print(f"(cảnh báo) Không đọc được lời thoại {name}: {e}", file=sys.stderr)
        return {}
    return {}


def _fallback_title(slug: str) -> str:
    """Tiêu đề dự phòng: ưu tiên TITLES trong app_backend, fallback = slug."""
    try:
        sys.path.insert(0, str(ROOT))
        import app_backend  # type: ignore

        return app_backend.TITLES.get(slug) or slug
    except Exception:
        return slug


def _seo_title(slug: str) -> str:
    """Title SEO/clickbait: ưu tiên CÂU HỎI trong hook lời thoại (gợi tò mò)."""
    segments = _load_segments(slug)
    if segments:
        # Ghép 1–2 đoạn đầu (hook) rồi tách câu, giữ dấu kết câu.
        text = " ".join(str(v).strip() for v in list(segments.values())[:2])
        sentences = [s.strip() for s in re.findall(r"[^.?!…]+[.?!…]?", text) if s.strip()]
        for s in sentences:  # ưu tiên câu hỏi
            if s.endswith("?"):
                return s
        if sentences:
            return sentences[0]
    return _fallback_title(slug)


def ensure_description(slug: str) -> Path:
    """Đảm bảo có noidung/mota/<slug>.txt (title SEO + hashtag). Không ghi đè nếu đã có."""
    MOTA_DIR.mkdir(parents=True, exist_ok=True)
    dest = MOTA_DIR / f"{slug}.txt"
    if dest.exists():
        return dest
    content = f"{_seo_title(slug)}\n\n{FIXED_HASHTAGS}\n"
    dest.write_text(content, encoding="utf-8")
    return dest


def main() -> int:
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("Dùng: python scenes/make_description.py <slug>", file=sys.stderr)
        return 2
    dest = ensure_description(sys.argv[1].strip())
    print(str(dest))  # dòng CUỐI = path (shell đọc bằng `tail -1`)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
