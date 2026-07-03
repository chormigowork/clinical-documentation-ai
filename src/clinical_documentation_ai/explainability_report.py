"""
Explainability reporting utilities for Clinical Documentation AI.

This module generates a lightweight Markdown report describing the main
steps and outputs of the pipeline execution.
"""

from typing import Any

from clinical_documentation_ai.utils import create_markdown_section, get_timestamp


def count_non_empty_items(value: Any, separator: str = ";") -> int:
    """
    Count non-empty items in a separated string.

    Args:
        value: Input value.
        separator: Separator used between items.

    Returns:
        Number of non-empty items.
    """
    if value is None:
        return 0

    items = [item.strip() for item in str(value).split(separator) if item.strip()]
    return len(items)


def generate_explainability_report(
    patient_record: dict[str, Any],
    prompt: str,
    raw_output: str,
    processed_output: str,
    generator_name: str = "MockClinicalGenerator",
) -> str:
    """
    Generate a Markdown explainability report for a pipeline execution.

    Args:
        patient_record: Structured clinical input.
        prompt: Generated prompt.
        raw_output: Raw AI-generated output.
        processed_output: Post-processed output.
        generator_name: Name of the generation backend used.

    Returns:
        Markdown report as string.
    """
    report = "# Explainability Report\n\n"

    report += create_markdown_section(
        "Pipeline Information",
        (
            f"- Execution time: {get_timestamp()}\n"
            f"- Generator: {generator_name}\n"
            f"- Patient ID: {patient_record.get('patient_id', 'Not available')}\n"
            f"- Document type: {patient_record.get('document_type', 'Not available')}"
        ),
    )

    report += create_markdown_section(
        "Input Summary",
        (
            f"- Diagnosis items: {count_non_empty_items(patient_record.get('diagnoses'))}\n"
            f"- Procedure items: {count_non_empty_items(patient_record.get('procedures'))}\n"
            f"- Additional information provided: "
            f"{'Yes' if patient_record.get('additional_information') else 'No'}"
        ),
    )

    report += create_markdown_section(
        "Prompt Summary",
        (
            f"- Characters: {len(prompt)}\n"
            f"- Words: {len(prompt.split())}\n"
            f"- Lines: {len(prompt.splitlines())}"
        ),
    )

    report += create_markdown_section(
        "Generation Summary",
        (
            "- Status: Completed successfully\n"
            f"- Raw output characters: {len(raw_output)}\n"
            f"- Raw output words: {len(raw_output.split())}"
        ),
    )

    report += create_markdown_section(
        "Post-processing Summary",
        (
            "- Placeholder removal: Applied\n"
            "- Section title normalisation: Applied\n"
            "- Whitespace normalisation: Applied\n"
            f"- Processed output characters: {len(processed_output)}\n"
            f"- Processed output words: {len(processed_output.split())}"
        ),
    )

    report += create_markdown_section(
        "Human Review",
        (
            "Human validation is required before any clinical use.\n\n"
            "This project is intended for educational, research and portfolio purposes only."
        ),
    )

    return report