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

from pipeline import ClinicalDocumentationPipeline
from utils import save_text_file


def load_sample_input(file_path: Path) -> dict:
    if not file_path.exists():
        raise FileNotFoundError(f"Sample input not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    print("=" * 60)
    print("Clinical Documentation AI")
    print("An Explainable AI Pipeline for Clinical Documentation")
    print("=" * 60)

    input_path = PROJECT_ROOT / "examples" / "sample_input.json"
    prompt_path = PROJECT_ROOT / "examples" / "generated_prompt.txt"
    raw_output_path = PROJECT_ROOT / "examples" / "raw_output.txt"
    processed_output_path = PROJECT_ROOT / "examples" / "sample_output.txt"

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