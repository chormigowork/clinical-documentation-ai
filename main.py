"""
Command-line entry point for Clinical Documentation AI.

Examples:
    python main.py
    python main.py --input examples/sample_input.json --output examples/custom_output.txt
"""

import argparse
import json
import logging
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"

sys.path.append(str(SRC_PATH))

from clinical_documentation_ai.config import (
    PROJECT_NAME,
    PROJECT_TAGLINE,
    SAMPLE_INPUT_PATH,
    GENERATED_PROMPT_PATH,
    RAW_OUTPUT_PATH,
    PROCESSED_OUTPUT_PATH,
    EXPLAINABILITY_REPORT_PATH,
    LOG_FORMAT,
    LOG_DATE_FORMAT,
)
from clinical_documentation_ai.explainability_report import (
    generate_explainability_report,
)
from clinical_documentation_ai.pipeline import ClinicalDocumentationPipeline
from clinical_documentation_ai.utils import save_text_file


def configure_logging() -> None:
    """
    Configure application logging.
    """
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=LOG_DATE_FORMAT,
    )


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Run the Clinical Documentation AI pipeline."
    )

    parser.add_argument(
        "--input",
        type=Path,
        default=SAMPLE_INPUT_PATH,
        help="Path to the input JSON file.",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=PROCESSED_OUTPUT_PATH,
        help="Path to save the processed clinical documentation.",
    )

    return parser.parse_args()


def load_sample_input(file_path: Path) -> dict:
    """
    Load patient input from a JSON file.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    """
    Execute the complete Clinical Documentation AI pipeline.
    """
    configure_logging()
    args = parse_args()

    logging.info("=" * 60)
    logging.info(PROJECT_NAME)
    logging.info(PROJECT_TAGLINE)
    logging.info("=" * 60)

    logging.info("Loading structured patient data...")
    patient_record = load_sample_input(args.input)

    logging.info("Running explainable AI pipeline...")
    pipeline = ClinicalDocumentationPipeline()
    result = pipeline.generate_document(patient_record)

    explainability_report = generate_explainability_report(
        patient_record=patient_record,
        prompt=result["prompt"],
        raw_output=result["raw_output"],
        processed_output=result["processed_output"],
    )

    logging.info("Saving generated prompt...")
    save_text_file(GENERATED_PROMPT_PATH, result["prompt"])

    logging.info("Saving raw AI output...")
    save_text_file(RAW_OUTPUT_PATH, result["raw_output"])

    logging.info("Saving processed clinical documentation...")
    save_text_file(args.output, result["processed_output"])

    logging.info("Saving explainability report...")
    save_text_file(EXPLAINABILITY_REPORT_PATH, explainability_report)

    logging.info("=" * 60)
    logging.info("Pipeline completed successfully")
    logging.info("=" * 60)
    logging.info("Input file: %s", args.input)
    logging.info("Prompt saved at: %s", GENERATED_PROMPT_PATH)
    logging.info("Raw output saved at: %s", RAW_OUTPUT_PATH)
    logging.info("Processed output saved at: %s", args.output)
    logging.info("Explainability report saved at: %s", EXPLAINABILITY_REPORT_PATH)


if __name__ == "__main__":
    main()