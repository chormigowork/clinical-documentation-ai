"""
Utility functions for the Clinical Documentation AI project.

This module contains reusable helper functions for file handling,
timestamps and text export.
"""

from datetime import datetime
from pathlib import Path


def ensure_directory(path: str | Path) -> Path:
    """
    Ensure that a directory exists.

    Args:
        path: Directory path.

    Returns:
        Path object for the created or existing directory.
    """
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)
    return directory


def read_text_file(file_path: str | Path) -> str:
    """
    Read a text file using UTF-8 encoding.

    Args:
        file_path: Path to the text file.

    Returns:
        File content as string.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    return path.read_text(encoding="utf-8")


def save_text_file(file_path: str | Path, content: str) -> None:
    """
    Save text content to a file using UTF-8 encoding.

    Args:
        file_path: Output file path.
        content: Text content to save.
    """
    path = Path(file_path)
    ensure_directory(path.parent)
    path.write_text(content, encoding="utf-8")


def get_timestamp() -> str:
    """
    Generate a readable timestamp.

    Returns:
        Current timestamp in YYYY-MM-DD HH:MM:SS format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_markdown_section(title: str, content: str) -> str:
    """
    Create a Markdown section.

    Args:
        title: Section title.
        content: Section content.

    Returns:
        Formatted Markdown section.
    """
    return f"## {title}\n\n{content.strip()}\n"