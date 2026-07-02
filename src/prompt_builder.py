"""
Prompt construction utilities for the Clinical Documentation AI pipeline.

This module transforms structured clinical information into controlled prompts
for AI-assisted clinical documentation generation.
"""

from typing import Any


DEFAULT_PROMPT_TEMPLATE = """
Generate a clinical discharge summary using anonymized patient data.

Patient ID: {patient_id}
Document type: {document_type}

Diagnosis:
{diagnoses}

Procedures:
{procedures}

Additional clinical information:
{additional_information}

Instructions:
- Generate a structured draft discharge summary.
- Do not invent patient names, hospital names or dates.
- Use only the information provided in the input.
- Keep the output clear, concise and clinically oriented.
- This is an AI-assisted draft and must be reviewed by a qualified professional.
""".strip()


def normalize_field(value: Any, default: str = "Not available") -> str:
    """
    Normalize a clinical field before inserting it into a prompt.

    Args:
        value: Input value.
        default: Text used when the input value is missing.

    Returns:
        Clean string representation of the input value.
    """
    if value is None:
        return default

    value_str = str(value).strip()

    if value_str == "" or value_str.lower() in {"nan", "none", "null"}:
        return default

    return value_str


def format_code_list(value: Any, default: str = "Not available") -> str:
    """
    Format a semicolon-separated list of clinical codes.

    Args:
        value: Clinical code field.
        default: Text used when no codes are available.

    Returns:
        Formatted clinical code list.
    """
    value_str = normalize_field(value, default="")

    if value_str == "":
        return default

    codes = [code.strip() for code in value_str.split(";") if code.strip()]

    if not codes:
        return default

    return "\n".join(f"- {code}" for code in codes)


def build_prompt(
    patient_id: Any,
    document_type: Any,
    diagnoses: Any,
    procedures: Any,
    additional_information: Any = (
        "Multiple diagnoses and procedures associated with the hospitalization "
        "episode were included as contextual information for the model."
    ),
    template: str = DEFAULT_PROMPT_TEMPLATE,
) -> str:
    """
    Build a controlled prompt for clinical documentation generation.

    Args:
        patient_id: Anonymized patient identifier.
        document_type: Type of clinical document.
        diagnoses: Diagnosis codes or descriptions.
        procedures: Procedure codes or descriptions.
        additional_information: Additional clinical context.
        template: Prompt template.

    Returns:
        A formatted prompt ready to be sent to a generative AI model.
    """
    return template.format(
        patient_id=normalize_field(patient_id),
        document_type=normalize_field(document_type),
        diagnoses=format_code_list(diagnoses),
        procedures=format_code_list(procedures),
        additional_information=normalize_field(additional_information),
    )


def build_prompt_from_record(record: dict[str, Any]) -> str:
    """
    Build a prompt from a dictionary-like clinical record.

    Expected keys:
        - patient_id
        - document_type
        - diagnoses
        - procedures
        - additional_information

    Args:
        record: Clinical record as a dictionary.

    Returns:
        A formatted clinical prompt.
    """
    return build_prompt(
        patient_id=record.get("patient_id"),
        document_type=record.get("document_type"),
        diagnoses=record.get("diagnoses"),
        procedures=record.get("procedures"),
        additional_information=record.get("additional_information"),
    )