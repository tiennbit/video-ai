"""Sinh giọng clone cho "Lon nước ngọt tối ưu". ~/voxcpm-venv/bin/python scenes/clone_narration_lonnuoc.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_lonnuoc import SEGMENTS

if __name__ == "__main__":
    run("lonnuoc", SEGMENTS)
