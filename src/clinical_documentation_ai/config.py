"""
Project configuration for Clinical Documentation AI.
"""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

PROJECT_NAME = "Clinical Documentation AI"
PROJECT_TAGLINE = "An Explainable AI Pipeline for Clinical Documentation"

EXAMPLES_DIR = PROJECT_ROOT / "examples"
DATA_DIR = PROJECT_ROOT / "data"
DOCS_DIR = PROJECT_ROOT / "docs"

SAMPLE_INPUT_PATH = EXAMPLES_DIR / "sample_input.json"
GENERATED_PROMPT_PATH = EXAMPLES_DIR / "generated_prompt.txt"
RAW_OUTPUT_PATH = EXAMPLES_DIR / "raw_output.txt"
PROCESSED_OUTPUT_PATH = EXAMPLES_DIR / "sample_output.txt"
EXPLAINABILITY_REPORT_PATH = EXAMPLES_DIR / "explainability_report.md"

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"