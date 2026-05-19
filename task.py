"""
task.py — Entry point for the CRISP associative memory experiment.

Usage:
    python task.py

Prompts the experimenter for a participant ID and language (fr/en),
runs the full experiment sequence (encoding, distractor, recognition),
saves results to data/ and prints performance metrics to the terminal.
"""
from experiment import Experiment
from analyse import (
    get_latest_file, load_results, calculate_metrics, print_metrics
)

if __name__ == "__main__":
    participant_id = input("Participant ID: ").strip()

    language = ""
    while language not in ["fr", "en"]:
        language = input("Language (fr/en): ").strip().lower()
        if language not in ["fr", "en"]:
            print("Invalid language. Please enter 'fr' or 'en'.")

    exp = Experiment(participant_id, language)
    exp.setup()
    try:
        exp.run_phases()
        exp.save_data()
    finally:
        exp.teardown()

    path = get_latest_file()
    results = load_results(path)
    metrics = calculate_metrics(results)
    print_metrics(metrics)
