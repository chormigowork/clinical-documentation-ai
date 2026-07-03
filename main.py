"""
Command-line entry point for Clinical Documentation AI.

Run:
    python main.py
"""

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"

# Allow imports from the project package
sys.path.append(str(SRC_PATH))

from clinical_documentation_ai.config import (
    PROJECT_NAME,
    PROJECT_TAGLINE,
    SAMPLE_INPUT_PATH,
    GENERATED_PROMPT_PATH,
    RAW_OUTPUT_PATH,
    PROCESSED_OUTPUT_PATH,
    EXPLAINABILITY_REPORT_PATH,
)

from clinical_documentation_ai.pipeline import ClinicalDocumentationPipeline
from clinical_documentation_ai.utils import save_text_file
from clinical_documentation_ai.explainability_report import (
    generate_explainability_report,
)


def load_sample_input(file_path: Path) -> dict:
    """
    Load sample patient input from a JSON file.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Sample input not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    """
    Execute the complete Clinical Documentation AI pipeline.
    """

    print("=" * 60)
    print(PROJECT_NAME)
    print(PROJECT_TAGLINE)
    print("=" * 60)

    print("✓ Loading structured patient data...")
    patient_record = load_sample_input(SAMPLE_INPUT_PATH)

    print("✓ Running explainable AI pipeline...")
    pipeline = ClinicalDocumentationPipeline()

    result = pipeline.generate_document(patient_record)

    explainability_report = generate_explainability_report(
        patient_record=patient_record,
        prompt=result["prompt"],
        raw_output=result["raw_output"],
        processed_output=result["processed_output"],
    )

    print("✓ Saving generated prompt...")
    save_text_file(GENERATED_PROMPT_PATH, result["prompt"])

    print("✓ Saving raw AI output...")
    save_text_file(RAW_OUTPUT_PATH, result["raw_output"])

    print("✓ Saving processed clinical documentation...")
    save_text_file(PROCESSED_OUTPUT_PATH, result["processed_output"])

    print("✓ Saving explainability report...")
    save_text_file(EXPLAINABILITY_REPORT_PATH, explainability_report)

    print("\n" + "=" * 60)
    print("Pipeline completed successfully")
    print("=" * 60)

    print(f"Prompt saved at: {GENERATED_PROMPT_PATH}")
    print(f"Raw output saved at: {RAW_OUTPUT_PATH}")
    print(f"Processed output saved at: {PROCESSED_OUTPUT_PATH}")
    print(f"Explainability report saved at: {EXPLAINABILITY_REPORT_PATH}")


if __name__ == "__main__":
    main()