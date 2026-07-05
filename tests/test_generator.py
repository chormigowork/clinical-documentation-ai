from clinical_documentation_ai.generator import generate_text


def test_generate_text():

    result = generate_text("Example prompt")

    assert isinstance(result, str)
    assert len(result) > 0