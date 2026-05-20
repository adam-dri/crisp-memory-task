"""
experiment.py — Experiment class managing a single session of the memory task.
"""
from utils.display import create_window, show_text_and_wait
from utils.data_handler import create_data_dir, build_output_path, save_results
from phases.encoding import load_stimuli, run_encoding
from phases.distractor import run_distractor
from phases.recognition import run_recognition
from config import N_RECOMBINED


class Experiment:
    """
    Represents a single associative memory experiment session.

    Attributes:
        participant_id (str): Participant identifier, e.g. "P01"
        language (str): "fr" or "en"
        win: PsychoPy window
        stimuli (list[dict]): Word pairs from the stimuli CSV
        results (list[dict]): Trial responses from the recognition phase
    """

    def __init__(self, participant_id: str, language: str):
        self.participant_id = participant_id
        self.language = language
        self.win = None
        self.stimuli = []
        self.results = []

    def setup(self) -> None:
        """Create data directory, open window and load stimuli."""
        create_data_dir()
        self.win = create_window()
        self.stimuli = load_stimuli(f"stimuli_{self.language}.csv")

    def run_phases(self) -> None:
        """Run encoding, distractor and recognition phases in order."""
        if self.language == "fr":
            welcome = (
                "Bienvenue !\n\nVous allez voir des paires de mots."
                "\nMémorisez-les.\n\nAppuyez sur ESPACE pour commencer."
            )
        else:
            welcome = (
                "Welcome!\n\nYou will see word pairs."
                "\nMemorize them.\n\nPress SPACE to start."
            )
        show_text_and_wait(self.win, welcome)

        run_encoding(self.win, self.stimuli)
        run_distractor(self.win, self.language)

        if self.language == "fr":
            instructions = (
                "PHASE DE RECONNAISSANCE\n\n"
                "Appuyez sur Y si la paire est identique.\n"
                "Appuyez sur N si la paire est recombinée.\n\n"
                "Appuyez sur ESPACE pour débuter."
            )
        else:
            instructions = (
                "RECOGNITION PHASE\n\n"
                "Press Y if the pair is intact.\n"
                "Press N if the pair is recombined.\n\n"
                "Press SPACE to begin."
            )
        show_text_and_wait(self.win, instructions)
        self.results = run_recognition(self.win, self.stimuli, N_RECOMBINED)

    def save_data(self) -> None:
        """Save results to data/PARTICIPANT_ID_TIMESTAMP.csv"""
        output_path = build_output_path(self.participant_id)
        save_results(output_path, self.results)

    def teardown(self) -> None:
        """Display goodbye screen and close the PsychoPy window."""
        if self.language == "fr":
            goodbye = "Merci !\n\nL'expérience est terminée."
        else:
            goodbye = "Thank you!\n\nThe experiment is over."

        show_text_and_wait(self.win, goodbye)
        self.win.close()
