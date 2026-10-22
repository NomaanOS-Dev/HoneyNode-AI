from openai import OpenAI


def analyze_honeypot_events(api_key, events):
    if not api_key:
        return "Enter your OpenAI API key in the sidebar."

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a defensive cyber deception analyst. "
                        "Analyze honeypot events, identify suspicious "
                        "behavior, explain evidence and uncertainty, "
                        "assign a 0-100 risk score, and recommend "
                        "defensive containment and monitoring steps. "
                        "Never claim an event is confirmed without evidence."
                    ),
                },
                {"role": "user", "content": str(events)},
            ],
            temperature=0.2,
            max_tokens=1200,
        )
        return response.choices[0].message.content or "No analysis returned."
    except Exception as e:
        return f"Analysis error: {e}"
