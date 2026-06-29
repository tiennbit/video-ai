"""Sinh giọng clone cho "Uranium E=mc²". ~/voxcpm-venv/bin/python scenes/clone_narration_uranium.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_uranium import SEGMENTS

if __name__ == "__main__":
    run("uranium", SEGMENTS)
