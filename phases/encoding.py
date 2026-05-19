"""
phases/encoding.py — Encoding phase of the associative memory task.
"""
from psychopy import core
import csv
from config import ENCODING_DISPLAY_TIME, FIXATION_DURATION
from utils.display import create_text_stimulus, show_fixation


def load_stimuli(stimuli_file: str) -> list[dict]:
    """
    Load word pairs from a CSV file.

    Args:
        stimuli_file (str): Path to the stimuli CSV, e.g. "stimuli_fr.csv"

    Returns:
        list[dict]: Each dict contains "word1" and "word2".
    """
    with open(stimuli_file, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def run_encoding(win, stimuli: list[dict]) -> None:
    """
    Display word pairs one by one for memorization.

    Each pair is preceded by a fixation cross and followed
    by a brief blank screen.

    Args:
        win (visual.Window): The experiment window.
        stimuli (list[dict]): Word pairs from load_stimuli().
    """
    stim = create_text_stimulus(win)

    for pair in stimuli:
        # Fixation cross
        show_fixation(win, FIXATION_DURATION)

        # Display pair
        stim.text = f"{pair['word1']} - {pair['word2']}"
        stim.draw()
        win.flip()
        core.wait(ENCODING_DISPLAY_TIME)

        # Blank screen between pairs
        win.flip()
        core.wait(0.3)
