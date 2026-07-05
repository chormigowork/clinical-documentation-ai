from clinical_documentation_ai.postprocessing import (
    remove_extra_whitespace,
    remove_placeholders,
    normalize_section_titles,
    postprocess_generated_text,
)


def test_remove_extra_whitespace():
    text = "Hello     world\n\n\nThis is   a test."
    result = remove_extra_whitespace(text)

    assert "     " not in result
    assert "\n\n\n" not in result


def test_remove_placeholders():
    text = "Patient: [Patient's Name]\nDate: [Admission Date]"
    result = remove_placeholders(text)

    assert "[Patient's Name]" not in result
    assert "[Admission Date]" not in result


def test_normalize_section_titles():
    text = "hospital course:\nPatient was stable."
    result = normalize_section_titles(text)

    assert "Hospital Course:" in result


def test_postprocess_generated_text():
    text = "DISCHARGE SUMMARY\n\n\nPatient: [Patient's Name]"
    result = postprocess_generated_text(text)

    assert "[Patient's Name]" not in result
    assert "\n\n\n" not in result


def test_postprocess_generated_text_raises_error_for_none():
    try:
        postprocess_generated_text(None)
    except ValueError as error:
        assert "Input text cannot be None" in str(error)