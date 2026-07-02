"""Sinh giọng clone cho "Bí mật phòng thì thầm" (elip). ~/voxcpm-venv/bin/python scenes/clone_narration_thitham.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_thitham import SEGMENTS

if __name__ == "__main__":
    run("thitham", SEGMENTS)
