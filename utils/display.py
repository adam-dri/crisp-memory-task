"""
utils/display.py — PsychoPy display utilities for the memory task.
"""
from psychopy import visual, event, core
from config import SCREEN_SIZE, BACKGROUND_COLOR, TEXT_COLOR, FONT_SIZE


def create_window() -> visual.Window:
    """
    Create and return the main experiment window.

    Returns:
        visual.Window: Configured PsychoPy window.
    """
    win = visual.Window(
        size=SCREEN_SIZE,
        color=BACKGROUND_COLOR,
        fullscr=False,
        units="height",
        allowGUI=False,
    )
    return win


def create_text_stimulus(
    win: visual.Window,
    text: str = ""
) -> visual.TextStim:
    """
    Create and return a reusable text stimulus.

    Args:
        win (visual.Window): The experiment window.
        text (str): Initial text content.

    Returns:
        visual.TextStim: Configured text stimulus.
    """
    return visual.TextStim(
        win=win,
        text=text,
        color=TEXT_COLOR,
        height=0.07
    )


def show_text_and_wait(win: visual.Window, text: str) -> None:
    """
    Display a message and wait for spacebar.

    Clears the event buffer before listening to avoid
    capturing keypresses from previous screens.

    Args:
        win (visual.Window): The experiment window.
        text (str): Message to display.
    """
    stim = create_text_stimulus(win, text)
    stim.draw()
    win.flip()
    core.wait(0.5)
    event.clearEvents()
    event.waitKeys(keyList=["space"])


def show_fixation(win: visual.Window, duration: float) -> None:
    """
    Display a fixation cross for a given duration.

    Args:
        win (visual.Window): The experiment window.
        duration (float): Display time in seconds.
    """
    stim = create_text_stimulus(win, "+")
    stim.draw()
    win.flip()
    core.wait(duration)
