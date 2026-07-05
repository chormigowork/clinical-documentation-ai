from clinical_documentation_ai.pipeline import ClinicalDocumentationPipeline


def test_pipeline():

    pipeline = ClinicalDocumentationPipeline()

    patient = {
        "patient_id": "P001",
        "document_type": "Discharge Summary",
        "diagnoses": "I10",
        "procedures": "0JH63XZ",
    }

    result = pipeline.generate_document(patient)

    assert "prompt" in result
    assert "raw_output" in result
    assert "processed_output" in result