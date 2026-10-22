# HoneyNode-AI

An AI-assisted cybersecurity deception and honeypot telemetry investigation application designed to review suspicious events and generate defensive threat assessments.

Developed by NomaanOS-Dev.

## 🚀 Key Features

- **Honeypot Event Analysis:** Review suspicious SSH login attempts, service connections, and port scans.
- **AI Threat Assessment:** Generate severity assessments and defensive recommendations.
- **CSV Import and Export:** Upload event data and download captured events for investigation.
- **Interactive Dashboard:** Explore security events using a Streamlit interface.
- **Defensive Monitoring Guidance:** Identify suspicious patterns and recommend containment measures.

## 🛠️ Tech Stack

Python 3.x | Streamlit | OpenAI API | Pandas

## 📦 Installation

```bash
git clone https://github.com/NomaanOS-Dev/HoneyNode-AI.git
cd HoneyNode-AI
pip install -r requirements.txt
streamlit run app.py

Configure your OpenAI API key in the application sidebar.

ð���️ Security Notice
Demo events are illustrative and do not represent verified attacks. Use only on systems and telemetry you are authorized to monitor. Validate AI-generated recommendations before taking action.
