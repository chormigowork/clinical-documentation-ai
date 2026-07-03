"""
Clinical Documentation AI pipeline.

This module orchestrates the complete workflow:

Clinical Data
      ↓
Prompt Builder
      ↓
Generation
      ↓
Post-processing
"""

from clinical_documentation_ai.generator import (
    MockClinicalGenerator,
    TextGenerator,
    generate_text,
)
from clinical_documentation_ai.postprocessing import postprocess_generated_text
from clinical_documentation_ai.prompt_builder import build_prompt_from_record


class ClinicalDocumentationPipeline:
    """
    End-to-end AI pipeline for clinical documentation generation.

    The pipeline coordinates prompt construction, text generation and
    post-processing while keeping each component independent.
    """

    def __init__(self, generator: TextGenerator | None = None) -> None:
        """
        Initialize the pipeline.

        Args:
            generator: Optional text generation backend. If None, a mock
                generator is used for local execution.
        """
        self.generator = generator or MockClinicalGenerator()

    def generate_document(self, patient_record: dict[str, Any]) -> dict[str, str]:
        """
        Execute the complete clinical documentation pipeline.

        Args:
            patient_record: Structured clinical information.

        Returns:
            Dictionary containing the generated prompt, raw output and
            processed output.
        """
        self._validate_patient_record(patient_record)

        prompt = build_prompt_from_record(patient_record)
        raw_output = generate_text(prompt, generator=self.generator)
        processed_output = postprocess_generated_text(raw_output)

        return {
            "prompt": prompt,
            "raw_output": raw_output,
            "processed_output": processed_output,
        }

    @staticmethod
    def _validate_patient_record(patient_record: dict[str, Any]) -> None:
        """
        Validate the minimum required fields for the pipeline.

        Args:
            patient_record: Structured clinical information.

        Raises:
            ValueError: If required fields are missing.
        """
        required_fields = [
            "patient_id",
            "document_type",
            "diagnoses",
            "procedures",
        ]

        missing_fields = [
            field for field in required_fields if field not in patient_record
        ]

        if missing_fields:
            raise ValueError(f"Missing required patient fields: {missing_fields}")