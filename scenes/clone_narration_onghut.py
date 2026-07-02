"""Sinh giọng clone cho "Ống hút cao tối đa 10 mét" (áp suất khí quyển). ~/voxcpm-venv/bin/python scenes/clone_narration_onghut.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_onghut import SEGMENTS

if __name__ == "__main__":
    run("onghut", SEGMENTS)
