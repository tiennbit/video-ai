#!/usr/bin/env bash
# Mở GUI xưởng video (Streamlit). Nhấp đúp file này trong Finder để chạy.
cd "$(dirname "$0")" || exit 1

if [ ! -x ".venv/bin/streamlit" ]; then
  echo "LỖI: không thấy .venv/bin/streamlit. Cần tạo venv và cài streamlit trước."
  echo "(Nhấn phím bất kỳ để đóng cửa sổ…)"; read -r -n 1
  exit 1
fi

.venv/bin/streamlit run app.py --server.address=127.0.0.1 --server.port=8501
status=$?

# Giữ cửa sổ mở để đọc lỗi nếu Streamlit thoát bất thường (khi nhấp đúp).
if [ "$status" -ne 0 ]; then
  echo ""
  echo "Streamlit đã thoát (mã $status). Nhấn phím bất kỳ để đóng…"
  read -r -n 1
fi
