import pytest
import csv
from pathlib import Path
from analyse import calculate_metrics


RESULTS_ALL_CORRECT = [
    {"correct": "True", "reaction_time": "1.0", "pair_type": "intact"},
    {"correct": "True", "reaction_time": "2.0", "pair_type": "intact"},
    {"correct": "True", "reaction_time": "1.5", "pair_type": "recombined"},
    {"correct": "True", "reaction_time": "0.8", "pair_type": "recombined"},
]

RESULTS_ALL_WRONG = [
    {"correct": "False", "reaction_time": "1.0", "pair_type": "intact"},
    {"correct": "False", "reaction_time": "2.0", "pair_type": "intact"},
    {"correct": "False", "reaction_time": "1.5", "pair_type": "recombined"},
    {"correct": "False", "reaction_time": "0.8", "pair_type": "recombined"},
]

RESULTS_MIXED = [
    {"correct": "True",  "reaction_time": "1.0", "pair_type": "intact"},
    {"correct": "False", "reaction_time": "2.0", "pair_type": "intact"},
    {"correct": "True",  "reaction_time": "1.5", "pair_type": "recombined"},
    {"correct": "True",  "reaction_time": "0.8", "pair_type": "recombined"},
]


def test_accuracy_all_correct():
    """All trials correct — expected accuracy is 100%."""
    metrics = calculate_metrics(RESULTS_ALL_CORRECT)
    assert metrics["accuracy"] == 100.0


def test_accuracy_all_wrong():
    """All trials wrong — expected accuracy is 0%."""
    metrics = calculate_metrics(RESULTS_ALL_WRONG)
    assert metrics["accuracy"] == 0.0


def test_accuracy_mixed():
    """3 out of 4 correct — expected accuracy is 75%."""
    metrics = calculate_metrics(RESULTS_MIXED)
    assert metrics["accuracy"] == 75.0


def test_mean_reaction_time():
    """Mean RT should be the arithmetic mean of all reaction times."""
    metrics = calculate_metrics(RESULTS_ALL_CORRECT)
    assert metrics["mean_rt"] == round((1.0 + 2.0 + 1.5 + 0.8) / 4, 4)


def test_accuracy_by_type_intact():
    """Only 1 of 2 intact pairs answered correctly — expected 50%."""
    metrics = calculate_metrics(RESULTS_MIXED)
    assert metrics["accuracy_by_type"]["intact"] == 50.0


def test_accuracy_by_type_recombined():
    """Both recombined pairs answered correctly — expected 100%."""
    metrics = calculate_metrics(RESULTS_MIXED)
    assert metrics["accuracy_by_type"]["recombined"] == 100.0
