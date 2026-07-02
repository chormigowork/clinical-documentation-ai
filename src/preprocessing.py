"""
Preprocessing utilities for the Clinical Documentation AI pipeline.

This module contains functions to load, validate and prepare clinical
documentation datasets before prompt construction and text generation.
"""

from pathlib import Path
from typing import Iterable

import pandas as pd


def load_csv(file_path: str | Path) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        file_path: Path to the CSV file.

    Returns:
        Loaded pandas DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    df = pd.read_csv(path)

    if df.empty:
        raise ValueError(f"The file is empty: {path}")

    return df


def validate_columns(df: pd.DataFrame, required_columns: Iterable[str]) -> None:
    """
    Validate that a DataFrame contains the required columns.

    Args:
        df: Input DataFrame.
        required_columns: Columns expected in the DataFrame.

    Raises:
        ValueError: If one or more required columns are missing.
    """
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")


def count_words(text: str) -> int:
    """
    Count the number of words in a text.

    Args:
        text: Input text.

    Returns:
        Number of words.
    """
    return len(str(text).split())


def count_characters(text: str) -> int:
    """
    Count the number of characters in a text.

    Args:
        text: Input text.

    Returns:
        Number of characters.
    """
    return len(str(text))


def count_lines(text: str) -> int:
    """
    Count the number of lines in a text.

    Args:
        text: Input text.

    Returns:
        Number of lines.
    """
    return len(str(text).splitlines())


def add_text_metrics(
    df: pd.DataFrame,
    text_column: str,
    prefix: str = "text",
) -> pd.DataFrame:
    """
    Add basic text metrics to a DataFrame.

    Args:
        df: Input DataFrame.
        text_column: Name of the column containing text.
        prefix: Prefix for the generated metric columns.

    Returns:
        DataFrame with added metric columns.
    """
    validate_columns(df, [text_column])

    processed_df = df.copy()
    processed_df[text_column] = processed_df[text_column].fillna("").astype(str)

    processed_df[f"{prefix}_word_count"] = processed_df[text_column].apply(count_words)
    processed_df[f"{prefix}_char_count"] = processed_df[text_column].apply(count_characters)
    processed_df[f"{prefix}_line_count"] = processed_df[text_column].apply(count_lines)

    return processed_df


def count_semicolon_items(text: str) -> int:
    """
    Count the number of semicolon-separated items in a text field.

    This is useful for fields containing ICD diagnosis or procedure codes.

    Args:
        text: Input text containing semicolon-separated values.

    Returns:
        Number of non-empty items.
    """
    if pd.isna(text) or str(text).strip() == "":
        return 0

    return len([item for item in str(text).split(";") if item.strip()])


def add_code_counts(
    df: pd.DataFrame,
    code_columns: Iterable[str],
) -> pd.DataFrame:
    """
    Add count columns for semicolon-separated clinical code fields.

    Args:
        df: Input DataFrame.
        code_columns: Columns containing semicolon-separated values.

    Returns:
        DataFrame with additional count columns.
    """
    processed_df = df.copy()

    for column in code_columns:
        if column in processed_df.columns:
            processed_df[f"{column}_count"] = processed_df[column].apply(
                count_semicolon_items
            )

    return processed_df


def prepare_raw_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare the RAW generated dataset for analysis.

    Expected text column:
        - GPT_Text

    Args:
        df: RAW dataset.

    Returns:
        Prepared DataFrame with text metrics.
    """
    validate_columns(df, ["GPT_Text"])

    prepared_df = df.copy()
    prepared_df["text_model"] = prepared_df["GPT_Text"].fillna("").astype(str)

    return add_text_metrics(prepared_df, "text_model", prefix="raw")


def prepare_processed_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare the PROCESSED dataset for analysis.

    Expected text column:
        - text

    Optional clinical columns:
        - icd10_diag
        - icd10_proc
        - target

    Args:
        df: Processed dataset.

    Returns:
        Prepared DataFrame with text metrics and clinical code counts.
    """
    validate_columns(df, ["text"])

    prepared_df = df.copy()
    prepared_df["text_model"] = prepared_df["text"].fillna("").astype(str)

    prepared_df = add_text_metrics(prepared_df, "text_model", prefix="processed")
    prepared_df = add_code_counts(
        prepared_df,
        code_columns=["icd10_diag", "icd10_proc", "target"],
    )

    return prepared_df