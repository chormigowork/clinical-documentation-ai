"""
Command-line entry point for Clinical Documentation AI.

Run:
    python main.py
"""

import json
from pathlib import Path
import sys


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
)

from clinical_documentation_ai.pipeline import ClinicalDocumentationPipeline
from clinical_documentation_ai.utils import save_text_file


def load_sample_input(file_path: Path) -> dict:
    if not file_path.exists():
        raise FileNotFoundError(f"Sample input not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    print("=" * 60)
    print(PROJECT_NAME)
    print(PROJECT_TAGLINE)
    print("=" * 60)

    input_path = SAMPLE_INPUT_PATH
    prompt_path = GENERATED_PROMPT_PATH
    raw_output_path = RAW_OUTPUT_PATH
    processed_output_path = PROCESSED_OUTPUT_PATH

    print("✓ Loading structured patient data...")
    patient_record = load_sample_input(input_path)

    print("✓ Running explainable AI pipeline...")
    pipeline = ClinicalDocumentationPipeline()
    result = pipeline.generate_document(patient_record)

    print("✓ Saving generated prompt...")
    save_text_file(prompt_path, result["prompt"])

    print("✓ Saving raw AI output...")
    save_text_file(raw_output_path, result["raw_output"])

    print("✓ Saving processed clinical documentation...")
    save_text_file(processed_output_path, result["processed_output"])

    print("\n" + "=" * 60)
    print("Pipeline completed successfully")
    print("=" * 60)
    print(f"Prompt saved at: {prompt_path}")
    print(f"Raw output saved at: {raw_output_path}")
    print(f"Processed output saved at: {processed_output_path}")


if __name__ == "__main__":
    main()