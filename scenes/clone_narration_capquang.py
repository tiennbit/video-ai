"""Sinh giọng clone cho "Cáp quang / phản xạ toàn phần". ~/voxcpm-venv/bin/python scenes/clone_narration_capquang.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_capquang import SEGMENTS

if __name__ == "__main__":
    run("capquang", SEGMENTS)
