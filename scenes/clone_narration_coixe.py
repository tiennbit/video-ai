"""Sinh giọng clone cho "Doppler còi xe". ~/voxcpm-venv/bin/python scenes/clone_narration_coixe.py"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _clone_common import run
from narration_texts_coixe import SEGMENTS

if __name__ == "__main__":
    run("coixe", SEGMENTS)
