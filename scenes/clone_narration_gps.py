"""Sinh giọng clone cho "GPS định vị". ~/voxcpm-venv/bin/python scenes/clone_narration_gps.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_gps import SEGMENTS

if __name__ == "__main__":
    run("gps", SEGMENTS)
