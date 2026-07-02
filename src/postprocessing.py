"""
Post-processing utilities for the Clinical Documentation AI pipeline.

This module normalizes raw AI-generated clinical documentation to improve
consistency, readability and downstream analysis.
"""

import re


def remove_extra_whitespace(text: str) -> str:
    """
    Remove duplicated spaces, tabs and excessive line breaks.

    Args:
        text: Input text.

    Returns:
        Text with normalized whitespace.
    """
    text = re.sub(r"[ \t]+", " ", str(text))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def remove_placeholders(text: str) -> str:
    """
    Remove common unresolved placeholders from generated clinical text.

    Args:
        text: Input text.

    Returns:
        Text without unresolved placeholder fragments.
    """
    placeholders = [
        r"\[Patient'?s Name\]",
        r"\[Admission Date\]",
        r"\[Discharge Date\]",
        r"\[Hospital Name\]",
        r"\[.*?\]",
    ]

    cleaned_text = str(text)

    for pattern in placeholders:
        cleaned_text = re.sub(pattern, "", cleaned_text, flags=re.IGNORECASE)

    return remove_extra_whitespace(cleaned_text)


def normalize_section_titles(text: str) -> str:
    """
    Normalize common clinical section titles.

    Args:
        text: Input text.

    Returns:
        Text with consistent section titles.
    """
    section_map = {
        "hospital course": "Hospital Course",
        "clinical impression": "Clinical Impression",
        "discharge summary": "Discharge Summary",
        "diagnosis": "Diagnosis",
        "procedures": "Procedures",
        "disclaimer": "Disclaimer",
    }

    normalized_text = str(text)

    for raw_title, clean_title in section_map.items():
        pattern = rf"(?im)^\s*{re.escape(raw_title)}\s*:?"
        normalized_text = re.sub(pattern, f"{clean_title}:", normalized_text)

    return normalized_text.strip()


def postprocess_generated_text(text: str) -> str:
    """
    Apply the full post-processing pipeline to generated clinical text.

    Args:
        text: Raw generated text.

    Returns:
        Cleaned and normalized clinical documentation draft.
    """
    if text is None:
        raise ValueError("Input text cannot be None.")

    processed_text = remove_placeholders(text)
    processed_text = normalize_section_titles(processed_text)
    processed_text = remove_extra_whitespace(processed_text)

    return processed_text


def create_raw_processed_pair(raw_text: str) -> dict[str, str]:
    """
    Create a dictionary containing both raw and processed versions of a text.

    Args:
        raw_text: Raw generated clinical text.

    Returns:
        Dictionary with raw_text and processed_text.
    """
    return {
        "raw_text": raw_text,
        "processed_text": postprocess_generated_text(raw_text),
    }