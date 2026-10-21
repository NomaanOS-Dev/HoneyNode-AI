import os
import pandas as pd
from openai import OpenAI

def analyze_traffic_logs(api_key, log_data):
    if not api_key:
        return "⚠️ Please provide a valid OpenAI API key in the sidebar configuration."
    
    try:
        client = OpenAI(api_key=api_key)
        prompt = f"""You are an elite AI Cybersecurity Architect. Analyze the following security telemetry / logs and provide a comprehensive threat assessment, risk score (0-100), MITRE ATT&CK mapping, and mitigation steps:

Logs / Data:
{log_data}
"""
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert AI security auditor and threat intelligence analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=1500
        ]
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error during AI analysis: {str(e)}"
