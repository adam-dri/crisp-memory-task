# config.py
import os
os.environ["PSYCHOPY_SILENT"] = "1"

from psychopy import monitors

# Window
SCREEN_SIZE = (1024, 768)
BACKGROUND_COLOR = "black"
TEXT_COLOR = "white"
FONT_SIZE = 40

# Timing (seconds)
ENCODING_DISPLAY_TIME = 3.0
DISTRACTOR_DURATION = 100.0
FIXATION_DURATION = 0.5

# Stimuli
N_PAIRS = 12
N_RECOMBINED = 6

# Keys
KEY_YES = "y"
KEY_NO = "n"

# Files
DATA_DIR = "data"

# Monitor setup - suppresses "Monitor specification not found" warning
mon = monitors.Monitor("testMonitor")
mon.setSizePix(SCREEN_SIZE)
mon.save()
