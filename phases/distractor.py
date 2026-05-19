"""
phases/distractor.py — Distractor phase to clear short-term memory.
"""
from psychopy import core, event
from config import DISTRACTOR_DURATION
from utils.display import create_text_stimulus


def run_distractor(win, language: str) -> None:
    """
    Display a countdown task to clear short-term memory.

    The participant counts backwards from 100. They can press SPACE
    to continue early, or the phase ends automatically after
    DISTRACTOR_DURATION seconds.

    Args:
        win (visual.Window): The experiment window.
        language (str): "fr" or "en"
    """
    if language == "fr":
        message = (
            "Comptez à rebours depuis 100.\n\n"
            "Appuyez sur ESPACE quand vous avez terminé."
        )
    else:
        message = (
            "Count backwards from 100.\n\n"
            "Press SPACE when you are done."
        )

    stim = create_text_stimulus(win, message)
    stim.draw()
    win.flip()

    event.clearEvents()
    event.waitKeys(keyList=["space"], maxWait=DISTRACTOR_DURATION)
