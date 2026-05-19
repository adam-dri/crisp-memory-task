"""
analyse.py — Compute and display performance metrics from experiment results.

Can be run standalone after task.py, or imported by task.py directly.

Usage:
    python analyse.py
"""
from pathlib import Path
from statistics import mean
import csv


def get_latest_file() -> Path:
    """
    Return the most recently modified CSV in data/.

    Raises:
        FileNotFoundError: If data/ contains no CSV files.
    """
    files = list(Path("data").glob("*.csv"))
    if not files:
        raise FileNotFoundError(
            "No results found in data/. Run task.py first."
        )
    return max(files, key=lambda f: f.stat().st_mtime)


def load_results(path: Path) -> list[dict]:
    """
    Load trial results from a CSV file.

    Args:
        path (Path): Path to the results CSV.

    Returns:
        list[dict]: One dict per trial.
    """
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def calculate_metrics(results: list[dict]) -> dict:
    """
    Calculate accuracy, mean RT and accuracy by pair type.

    Args:
        results (list[dict]): Trial results from load_results().

    Returns:
        dict: accuracy, mean_rt, accuracy_by_type (intact/recombined).
    """
    correct_trials = [r for r in results if r["correct"] == "True"]
    accuracy = len(correct_trials) / len(results) * 100

    times = [float(r["reaction_time"]) for r in results]
    mean_rt = mean(times)

    accuracy_by_type = {}
    for pair_type in ["intact", "recombined"]:
        trials = [r for r in results if r["pair_type"] == pair_type]
        correct = [r for r in trials if r["correct"] == "True"]
        accuracy_by_type[pair_type] = len(correct) / len(trials) * 100

    return {
        "accuracy": round(accuracy, 1),
        "mean_rt": round(mean_rt, 4),
        "accuracy_by_type": accuracy_by_type
    }


def print_metrics(metrics: dict) -> None:
    """
    Print metrics to the terminal.

    Args:
        metrics (dict): Output of calculate_metrics().
    """
    print("\n=== RESULTS ===")
    print(f"Accuracy        : {metrics['accuracy']}%")
    print(f"Mean RT         : {metrics['mean_rt']}s")
    print("\nAccuracy by pair type:")
    for pair_type, acc in metrics["accuracy_by_type"].items():
        print(f"  {pair_type:<12}: {round(acc, 1)}%")


if __name__ == "__main__":
    try:
        path = get_latest_file()
        results = load_results(path)
        metrics = calculate_metrics(results)
        print_metrics(metrics)
    except FileNotFoundError as e:
        print(f"Error: {e}")
