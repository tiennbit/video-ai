"""Sinh giọng clone cho "Cú xoáy của Messi" (Magnus). ~/voxcpm-venv/bin/python scenes/clone_narration_magnus.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_magnus import SEGMENTS

if __name__ == "__main__":
    run("magnus", SEGMENTS)
