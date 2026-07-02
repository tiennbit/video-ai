"""Sinh giọng clone cho "Tai nghe khử ồn" (giao thoa). ~/voxcpm-venv/bin/python scenes/clone_narration_chongon.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_chongon import SEGMENTS

if __name__ == "__main__":
    run("chongon", SEGMENTS)
