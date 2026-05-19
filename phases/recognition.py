"""
phases/recognition.py — Recognition phase of the associative memory task.
"""
import random
from psychopy import core, event
from config import FIXATION_DURATION, KEY_YES, KEY_NO
from utils.display import create_text_stimulus, show_fixation


def generate_test_pairs(stimuli: list[dict], n_recombined: int) -> list[dict]:
    """
    Build the test list from intact pairs and recombined foils.

    Recombined pairs reuse words from the stimuli but in new combinations
    the participant has never seen, making them plausible but incorrect.

    Args:
        stimuli (list[dict]): Original word pairs from the encoding phase.
        n_recombined (int): Number of foil pairs to generate.

    Returns:
        list[dict]: Shuffled list of intact and recombined pairs,
                    each with keys word1, word2 and pair_type.
    """
    test_pairs = [
        {"word1": p["word1"], "word2": p["word2"], "pair_type": "intact"}
        for p in stimuli
    ]

    words2 = [p["word2"] for p in stimuli]
    random.shuffle(words2)

    foils = random.sample(stimuli, n_recombined)
    for i, pair in enumerate(foils):
        test_pairs.append({
            "word1": pair["word1"],
            "word2": words2[i],
            "pair_type": "recombined"
        })

    random.shuffle(test_pairs)
    return test_pairs


def run_recognition(win, stimuli: list[dict], n_recombined: int) -> list[dict]:
    """
    Run the recognition phase and return trial-by-trial results.

    For each pair, the participant presses KEY_YES if they recognize
    the pair from the encoding phase, or KEY_NO if it seems new.
    Reaction time is measured from stimulus onset to keypress.

    Args:
        win (visual.Window): The experiment window.
        stimuli (list[dict]): Word pairs from the encoding phase.
        n_recombined (int): Number of foil pairs to include.

    Returns:
        list[dict]: One dict per trial with word1, word2, pair_type,
                    response, correct and reaction_time.
    """
    test_pairs = generate_test_pairs(stimuli, n_recombined)
    stim = create_text_stimulus(win)
    results = []

    for pair in test_pairs:
        show_fixation(win, FIXATION_DURATION)

        stim.text = f"{pair['word1']} - {pair['word2']}"
        stim.draw()
        win.flip()

        start_time = core.getTime()
        keys = event.waitKeys(keyList=[KEY_YES, KEY_NO])
        reaction_time = core.getTime() - start_time

        response = keys[0]
        correct = (
            (response == KEY_YES and pair["pair_type"] == "intact") or
            (response == KEY_NO and pair["pair_type"] == "recombined")
        )

        results.append({
            "word1": pair["word1"],
            "word2": pair["word2"],
            "pair_type": pair["pair_type"],
            "response": response,
            "correct": correct,
            "reaction_time": round(reaction_time, 4)
        })

    return results
