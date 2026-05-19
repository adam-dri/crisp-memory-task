import csv
import pytest
from pathlib import Path
from utils.data_handler import (
    create_data_dir, build_output_path, save_results, FIELDNAMES
)


def test_create_data_dir(tmp_path, monkeypatch):
    """data/ directory should be created if it doesn't exist."""
    monkeypatch.chdir(tmp_path)
    create_data_dir()
    assert (tmp_path / "data").is_dir()


def test_create_data_dir_already_exists(tmp_path, monkeypatch):
    """create_data_dir should not raise if data/ already exists."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / "data").mkdir()
    create_data_dir()
    assert (tmp_path / "data").is_dir()


def test_build_output_path_format():
    """Output path should follow the pattern data/ID_YYYYMMDD_HHMMSS.csv"""
    path = build_output_path("P01")
    assert path.parent == Path("data")
    assert path.name.startswith("P01_")
    assert path.suffix == ".csv"


def test_save_results(tmp_path):
    """Results should be written to CSV with correct headers and values."""
    results = [
        {
            "word1": "CHIEN",
            "word2": "NUAGE",
            "pair_type": "intact",
            "response": "y",
            "correct": True,
            "reaction_time": 0.8432
        }
    ]
    output = tmp_path / "test_results.csv"
    save_results(output, results)

    with open(output, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 1
    assert rows[0]["word1"] == "CHIEN"
    assert rows[0]["pair_type"] == "intact"
    assert rows[0]["response"] == "y"


def test_save_results_headers(tmp_path):
    """CSV file should contain all expected column headers."""
    output = tmp_path / "test_headers.csv"
    save_results(output, [])

    with open(output, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == FIELDNAMES
