"""Sinh giọng clone cho "Liều thuốc và giới hạn an toàn" (cấp số nhân). ~/voxcpm-venv/bin/python scenes/clone_narration_lieuthuoc.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_lieuthuoc import SEGMENTS

if __name__ == "__main__":
    run("lieuthuoc", SEGMENTS)
