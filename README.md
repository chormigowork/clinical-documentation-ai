# 🩺 Clinical Documentation AI

### *From Clinical Data to Clinical Documentation*

> **End-to-End AI Pipeline for Automated Clinical Documentation using Generative AI**

---

## Overview

Clinical Documentation AI is an end-to-end Artificial Intelligence project that explores how Generative AI can support healthcare professionals by transforming structured clinical information into high-quality draft clinical documentation.

Rather than replacing clinicians, the objective of this project is to demonstrate how AI can reduce administrative workload while maintaining transparency, reproducibility and human supervision throughout the documentation process.

Originally developed as my Final Degree Project in Applied Data Science (**final grade: 9.01/10**), this repository has been redesigned as an open-source portfolio project with a stronger focus on software engineering, documentation and reproducibility.

---

# The Problem

Clinical documentation is one of the most time-consuming administrative tasks in modern healthcare.

Healthcare professionals spend a significant amount of time writing discharge summaries and other clinical documents, reducing the time available for direct patient care.

Although Large Language Models have demonstrated remarkable text generation capabilities, their integration into clinical workflows requires transparency, traceability and human validation.

This project explores one possible approach.

---

# The Solution

Clinical Documentation AI implements a complete AI pipeline capable of:

- Processing structured clinical data
- Preparing optimized prompts
- Generating draft clinical documentation using Generative AI
- Applying post-processing techniques
- Producing consistent and reproducible discharge summaries

The project focuses on explainability and reproducibility rather than raw text generation.

---

# Key Features

- ✅ Structured clinical data preprocessing
- ✅ Prompt Engineering for medical text generation
- ✅ AI-assisted discharge summary generation
- ✅ Post-processing pipeline
- ✅ Modular project architecture
- ✅ Reproducible workflow
- ✅ Human-in-the-loop philosophy
- ✅ Educational and research-oriented implementation

---

# Project Workflow

```text
Structured Clinical Data
            │
            ▼
Data Preprocessing
            │
            ▼
Prompt Builder
            │
            ▼
Generative AI
            │
            ▼
Post-processing
            │
            ▼
Clinical Documentation
```

---

# Repository Structure

```text
clinical-documentation-ai/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_Data_Exploration.ipynb
│   ├── 02_Data_Preparation.ipynb
│   ├── 03_Prompt_Engineering.ipynb
│   └── 04_Generation.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── prompt_builder.py
│   ├── generator.py
│   ├── postprocessing.py
│   └── utils.py
│
├── docs/
│   ├── architecture.png
│   ├── workflow.png
│   └── screenshots/
│
└── examples/
    ├── input.json
    ├── generated_report.txt
    └── comparison.md
```

---

# Technology Stack

### Programming

- Python

---

### Data Processing

- Pandas
- NumPy

---

### Artificial Intelligence

- Generative AI
- Prompt Engineering
- Natural Language Processing (NLP)

---

### Dataset

- MIMIC-IV

---

### Development Environment

- Google Colab
- Jupyter Notebook
- Git
- GitHub

---

# Example Pipeline

Input

```
Clinical structured data
ICD-10 diagnosis
ICD-10 procedures
Patient information
```

↓

Prompt construction

↓

Generative AI

↓

Post-processing

↓

Draft discharge summary

---

# Project Goals

The main objective of this repository is to demonstrate how Artificial Intelligence can be integrated into healthcare documentation workflows through a transparent and reproducible approach.

The project prioritises:

- Explainability
- Reproducibility
- Human supervision
- Software engineering best practices
- Responsible AI principles

---

# Roadmap

## Completed

- [x] Clinical data preprocessing
- [x] Prompt Engineering
- [x] Clinical text generation
- [x] Post-processing workflow
- [x] Final Degree Project completed

## Next Steps

- [ ] Repository refactoring
- [ ] Code modularisation
- [ ] Architecture documentation
- [ ] Interactive web interface
- [ ] Docker deployment
- [ ] Local LLM support
- [ ] Medical terminology validation
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] CI/CD pipeline
- [ ] Unit testing

---

# Disclaimer

This repository is intended exclusively for educational, research and portfolio purposes.

It is **not** a medical device, **not** intended for clinical diagnosis and **must not** be used for medical decision-making.

Any AI-generated clinical documentation should always be reviewed and validated by qualified healthcare professionals.

---

# Future Improvements

Future versions of the project may include:

- RAG-based knowledge retrieval
- Medical terminology validation
- FHIR interoperability
- Explainable AI (XAI)
- Local deployment using open-source LLMs
- Interactive dashboard
- Multi-language support
- Human feedback loop

---

# Author

**Carles Hormigo**

Applied Data Science Graduate

Artificial Intelligence • Machine Learning • Generative AI • Python

📍 Girona, Spain

---

> *"The best way to understand Artificial Intelligence is to build solutions that solve real problems."*
