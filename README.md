# 🩺 Clinical Documentation AI

### *An Explainable AI Pipeline for Clinical Document Generation*

> From Clinical Data to Clinical Documentation

---

## Overview

Clinical Documentation AI is an explainable AI pipeline that explores how Generative AI can support the creation of draft clinical documentation from structured clinical data.

The project is based on a modular architecture designed around transparency, traceability, post-processing and human supervision.

It was originally developed as my Final Degree Project in Applied Data Science, with a final grade of **9.01/10**, and is now being redesigned as a professional open-source portfolio project.

---

## Design Principles

- **Human supervision first**
- **Transparency by design**
- **Modular architecture**
- **Reproducible workflow**
- **Responsible AI**
- **Educational and research-oriented use**

---

## The Problem

Clinical documentation is one of the most time-consuming administrative tasks in healthcare.

Healthcare professionals often spend a significant amount of time writing discharge summaries and clinical reports, reducing the time available for direct patient care.

Generative AI can help with this process, but its use in healthcare requires careful design due to risks such as hallucinations, lack of traceability and factual inconsistencies.

---

## The Solution

This project implements a modular AI-assisted workflow:

```text
Structured Clinical Data
        ↓
Data Preprocessing
        ↓
Prompt Builder
        ↓
Generative AI Model
        ↓
Post-processing
        ↓
Draft Clinical Documentation
        ↓
Human Review
```

The goal is not to replace clinicians, but to explore how AI can assist documentation tasks in a transparent and controlled way.

---

## Key Features

- Structured clinical data preprocessing
- Prompt Engineering for clinical text generation
- AI-assisted draft discharge summary generation
- Post-processing and text normalisation
- Modular Python architecture
- Human-in-the-loop philosophy
- Designed for reproducibility and future extension

---

## Repository Structure

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
├── docs/
│   ├── images/
│   ├── diagrams/
│   └── screenshots/
│
├── examples/
│   ├── sample_input.json
│   └── sample_output.txt
│
├── notebooks/
│
├── src/
│   ├── preprocessing.py
│   ├── prompt_builder.py
│   ├── generator.py
│   ├── postprocessing.py
│   ├── evaluation.py
│   ├── pipeline.py
│   └── utils.py
│
└── tests/
```

---

## Technology Stack

**Programming**

Python

**Data Processing**

Pandas · NumPy

**Artificial Intelligence**

Generative AI · Prompt Engineering · NLP

**Development**

Google Colab · Jupyter Notebook · Git · GitHub

**Dataset**

MIMIC-IV / MIMIC-IV-Note

---

## Project Status

🚧 Work in progress.

Current version: **v0.1 – Core architecture**

---

## Roadmap

### v0.1 — Foundation

- [x] Repository structure
- [x] README initial version
- [x] Preprocessing module
- [x] Prompt builder module
- [ ] Generator module
- [ ] Post-processing module
- [ ] Pipeline module

### v0.5 — Executable Pipeline

- [ ] Sample input
- [ ] Sample output
- [ ] End-to-end local execution
- [ ] Basic CLI

### v1.0 — Portfolio Release

- [ ] Architecture diagram
- [ ] Project banner
- [ ] Screenshots
- [ ] Complete documentation
- [ ] Example generated report

### v2.0 — Interactive Demo

- [ ] Web interface
- [ ] Upload CSV or JSON
- [ ] Visualise prompt, raw output and processed output
- [ ] Export clinical draft

---

## Disclaimer

This repository is intended exclusively for educational, research and portfolio purposes.

It is **not** a medical device, **not** intended for clinical diagnosis and **must not** be used for medical decision-making.

Any AI-generated clinical documentation should always be reviewed and validated by qualified healthcare professionals.

---

## Author

**Carles Hormigo**

Applied Data Science Graduate  
Artificial Intelligence · Machine Learning · Generative AI · Python

📍 Girona, Spain

---

> *The best way to understand Artificial Intelligence is to build solutions that solve real problems.*