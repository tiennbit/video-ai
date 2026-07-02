"""Sinh giọng clone cho "Chim đậu dây điện". ~/voxcpm-venv/bin/python scenes/clone_narration_chimday.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_chimday import SEGMENTS

if __name__ == "__main__":
    run("chimday", SEGMENTS)
