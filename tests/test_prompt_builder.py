from clinical_documentation_ai.prompt_builder import build_prompt


def test_build_prompt_returns_string():

    prompt = build_prompt(
        patient_id="P001",
        document_type="Discharge Summary",
        diagnoses="I10",
        procedures="0JH63XZ",
    )

    assert isinstance(prompt, str)
    assert "P001" in prompt
    assert "Discharge Summary" in prompt