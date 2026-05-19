"""
utils/data_handler.py — File I/O utilities for saving experiment results.
"""
import csv
from pathlib import Path
from datetime import datetime

FIELDNAMES = [
    "word1", "word2", "pair_type", "response", "correct", "reaction_time"
]


def create_data_dir() -> None:
    """Create the data/ directory if it doesn't exist."""
    Path("data").mkdir(exist_ok=True)


def build_output_path(participant_id: str) -> Path:
    """
    Return a timestamped path for the results CSV.

    Args:
        participant_id (str): Participant identifier, e.g. "P01"

    Returns:
        Path: e.g. data/P01_20260517_143022.csv
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return Path("data") / f"{participant_id}_{timestamp}.csv"


def save_results(path: Path, results: list[dict]) -> None:
    """
    Write trial results to a CSV file.

    Args:
        path (Path): Output file path from build_output_path().
        results (list[dict]): Trial data from the recognition phase.
    """
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(results)
