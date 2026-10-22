# HoneyNode-AI

AI-assisted honeypot telemetry analysis for reviewing suspicious activity, identifying attacker behavior patterns, and generating defensive recommendations.

Developed by NomaanOS-Dev.

## Overview

HoneyNode-AI is a Streamlit-based security workflow for analyzing captured honeypot events. It allows users to upload CSV telemetry, review suspicious event patterns, and generate an AI-assisted threat assessment with recommended monitoring and containment steps.

## Key Features

- Honeypot event analysis for repeated login failures, port scans, and decoy service activity
- AI-powered threat assessment and risk scoring
- CSV upload and export support for investigation workflows
- Interactive dashboard for reviewing telemetry in context
- Defensive guidance for containment, monitoring, and escalation
- Sample event data for testing without uploading real logs

## Tech Stack

- Python 3.x
- Streamlit
- OpenAI API
- Pandas

## Project Structure

```text
HoneyNode-AI/
├── app.py           # Streamlit interface and event handling
├── analyzer.py      # OpenAI-based honeypot analysis logic
├── requirements.txt # Python dependencies
├── README.md        # Project documentation
└── .gitignore       # Repository ignore rules (if present)
```

## Installation

```bash
git clone https://github.com/NomaanOS-Dev/HoneyNode-AI.git
cd HoneyNode-AI
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Usage

1. Launch the app with `streamlit run app.py`.
2. Enter your OpenAI API key in the sidebar.
3. Either load the built-in sample events or upload a CSV file.
4. Review the event table in the dashboard.
5. Click the analysis button to generate an AI threat assessment.
6. Export captured events as needed for further investigation.

## Configuration

The app expects an OpenAI API key in the sidebar before running AI-based analysis. The project uses the `gpt-4o-mini` model via the OpenAI Python SDK.

## Security Notice

Demo events are illustrative and do not represent verified attacks. Use only on systems and telemetry you are authorized to monitor. Validate AI-generated recommendations before taking any defensive action.

## Notes

This project is intended as a security assistance tool and is not a replacement for formal incident response, detection engineering, or analyst review.
