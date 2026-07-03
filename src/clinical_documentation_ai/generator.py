"""
Generation utilities for the Clinical Documentation AI pipeline.

This module defines an abstract text generation layer so the pipeline can work
with different AI providers or mock generators without changing the rest of
the project.
"""

from typing import Protocol


class TextGenerator(Protocol):
    """
    Protocol for text generation models.

    Any generator used in the pipeline must implement the generate method.
    """

    def generate(self, prompt: str) -> str:
        """
        Generate text from a prompt.

        Args:
            prompt: Input prompt.

        Returns:
            Generated text.
        """
        ...


class MockClinicalGenerator:
    """
    Mock generator used for local testing and portfolio demonstration.

    This class does not call any external AI model. It returns a deterministic
    draft clinical document so the pipeline can be executed safely without API
    keys or external dependencies.
    """

    def generate(self, prompt: str) -> str:
        """
        Generate a mock clinical discharge summary.

        Args:
            prompt: Structured clinical prompt.

        Returns:
            Mock generated clinical documentation.
        """
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        return (
            "DISCHARGE SUMMARY\n\n"
            "This is an AI-assisted draft generated from structured clinical "
            "information.\n\n"
            "Hospital Course:\n"
            "The patient episode includes multiple diagnoses and procedures "
            "provided as structured input data.\n\n"
            "Clinical Impression:\n"
            "The generated documentation should be reviewed by a qualified "
            "healthcare professional before any clinical use.\n\n"
            "Disclaimer:\n"
            "This output is generated for educational and portfolio purposes only."
        )


def generate_text(prompt: str, generator: TextGenerator | None = None) -> str:
    """
    Generate clinical documentation using a text generator.

    Args:
        prompt: Structured clinical prompt.
        generator: Text generation backend. If None, MockClinicalGenerator is used.

    Returns:
        Generated clinical documentation.
    """
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    selected_generator = generator or MockClinicalGenerator()

    return selected_generator.generate(prompt)