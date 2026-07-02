"""
Clinical Documentation AI Pipeline.

This module orchestrates the complete workflow:

Clinical Data
      ↓
Preprocessing
      ↓
Prompt Builder
      ↓
Generation
      ↓
Post-processing
"""

from typing import Any

from preprocessing import prepare_processed_dataset
from prompt_builder import build_prompt_from_record
from generator import generate_text
from postprocessing import postprocess_generated_text


class ClinicalDocumentationPipeline:
    """
    End-to-end AI pipeline for clinical documentation generation.
    """

    def __init__(self):
        """Initialize the pipeline."""
        pass

    def generate_document(self, patient_record: dict[str, Any]) -> dict[str, str]:
        """
        Execute the complete pipeline.

        Args:
            patient_record:
                Structured clinical information.

        Returns:
            Dictionary containing prompt, raw output and processed output.
        """

        prompt = build_prompt_from_record(patient_record)

        raw_output = generate_text(prompt)

        processed_output = postprocess_generated_text(raw_output)

        return {
            "prompt": prompt,
            "raw_output": raw_output,
            "processed_output": processed_output,
        }