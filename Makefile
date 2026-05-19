.PHONY: help install run analyse test clean clean-data

help:
	@echo "Available targets:"
	@echo "  install     Install dependencies"
	@echo "  run         Run the experiment"
	@echo "  analyse     Display results from the last session"
	@echo "  test        Run unit tests"
	@echo "  clean       Remove temporary Python files"
	@echo "  clean-data  Remove all results from data/"

install:
	pip install -r requirements.txt

run:
	python task.py

analyse:
	python analyse.py

test:
	pytest tests/ -v

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -name "*.pyc" -delete

clean-data:
	rm -rf data/*.csv
