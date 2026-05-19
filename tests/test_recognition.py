import pytest
from phases.recognition import generate_test_pairs


STIMULI = [
    {"word1": "CHIEN", "word2": "NUAGE"},
    {"word1": "POMME", "word2": "BUREAU"},
    {"word1": "LUNE",  "word2": "CHAPEAU"},
    {"word1": "ARBRE", "word2": "BOUTON"},
    {"word1": "LAMPE", "word2": "RIVIÈRE"},
    {"word1": "PORTE", "word2": "ÉTOILE"},
]


def test_total_pairs_count():
    """Total test pairs should equal intact + recombined."""
    pairs = generate_test_pairs(STIMULI, n_recombined=3)
    assert len(pairs) == len(STIMULI) + 3


def test_intact_pairs_count():
    """All stimuli should appear as intact pairs."""
    pairs = generate_test_pairs(STIMULI, n_recombined=3)
    intact = [p for p in pairs if p["pair_type"] == "intact"]
    assert len(intact) == len(STIMULI)


def test_recombined_words_exist_in_stimuli():
    """Words in recombined pairs should come from the original stimuli."""
    original_words = set()
    for p in STIMULI:
        original_words.add(p["word1"])
        original_words.add(p["word2"])

    pairs = generate_test_pairs(STIMULI, n_recombined=3)
    recombined = [p for p in pairs if p["pair_type"] == "recombined"]
    for pair in recombined:
        assert pair["word1"] in original_words
        assert pair["word2"] in original_words
