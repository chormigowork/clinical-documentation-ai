from pathlib import Path

from clinical_documentation_ai.utils import (
    create_markdown_section,
    ensure_directory,
    get_timestamp,
    save_text_file,
    read_text_file,
)


def test_ensure_directory(tmp_path):
    directory = tmp_path / "new_folder"

    ensure_directory(directory)

    assert directory.exists()
    assert directory.is_dir()


def test_save_and_read_text(tmp_path):
    file_path = tmp_path / "example.txt"

    save_text_file(file_path, "Hello World")

    content = read_text_file(file_path)

    assert content == "Hello World"


def test_create_markdown_section():
    markdown = create_markdown_section(
        "Example",
        "This is a test."
    )

    assert "## Example" in markdown
    assert "This is a test." in markdown


def test_timestamp_format():
    timestamp = get_timestamp()

    assert len(timestamp) == 19
    assert "-" in timestamp
    assert ":" in timestamp