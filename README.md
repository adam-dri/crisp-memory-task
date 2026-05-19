![Python](https://img.shields.io/badge/Python-3.11-blue)
![PsychoPy](https://img.shields.io/badge/PsychoPy-2023-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-14%20passed-brightgreen)


# CRISP Memory Task

A word-pair associative memory task built with PsychoPy, inspired by the
research conducted at the CRISP lab (Douglas Research Centre, McGill University).

Associative memory, the ability to link two unrelated items, is one of the
core cognitive deficits studied in schizophrenia research. This task measures
it by presenting word pairs at encoding, then testing whether participants can
distinguish intact pairs from recombined foils at retrieval.

## How it works

**Encoding:** Participants see 12 word pairs displayed one at a time
(e.g. CHIEN - NUAGE). Each pair is shown for 3 seconds.

**Distractor:** Participants count backwards from 100 to clear short-term
memory. They can press SPACE when done, or the phase ends automatically
after 100 seconds.

**Recognition:** Participants see 18 pairs, the 12 original intact pairs
plus 6 recombined foils (words seen before, but in new combinations).
They press Y (yes, same pair) or N (no, recombined).

**Results:** Accuracy, mean reaction time and accuracy by pair type
(intact vs recombined) are printed to the terminal and saved to a CSV.

## Requirements

- Python 3.11
- PsychoPy 2023

## Setup

```bash
# Mac/Linux
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Windows
python3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python task.py
```

You will be prompted for a participant ID and language (fr/en).
Results are saved automatically to `data/PARTICIPANT_ID_TIMESTAMP.csv`.

## Analyse

```bash
python analyse.py
```

Prints accuracy, mean reaction time and accuracy by pair type
for the most recent session.

## Tests

```bash
pytest tests/ -v
```


## Makefile (Mac/Linux)

```bash
make install    # Install dependencies
make run        # Run the experiment
make analyse    # Display results from the last session
make test       # Run unit tests
make clean      # Remove temporary Python files
make clean-data # Remove all results from data/
```

**Windows:** use the commands directly, e.g. `python task.py`, `pytest tests/ -v`.

## Project Structure

```
crisp_memory_task/
├── task.py          # Entry point
├── experiment.py    # Experiment class
├── analyse.py       # Performance metrics
├── config.py        # Parameters and constants
├── phases/          # Encoding, distractor, recognition
├── utils/           # Display and file I/O
├── tests/           # Unit tests
├── stimuli_fr.csv   # French word pairs
└── stimuli_en.csv   # English word pairs
```

## Author

**Adam Driouich**

- GitHub: [@adam-dri](https://github.com/adam-dri)
- LinkedIn: [adam-driouich](https://linkedin.com/in/adam-driouich)

## License

MIT License - see [LICENSE](LICENSE).
