import streamlit as st
import pandas as pd
from analyzer import analyze_honeypot_events

st.set_page_config(
    page_title="HoneyNode-AI",
    page_icon="🍯",
    layout="wide",
)

st.title("🍯 HoneyNode-AI")
st.subheader("Autonomous Deception & Threat Capture Engine")
st.caption(
    "Review honeypot telemetry, investigate suspicious activity, "
    "and generate AI-assisted defensive recommendations."
)

with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("OpenAI API Key", type="password")

sample_events = [
    {
        "timestamp": "2026-10-22 09:10:12",
        "source_ip": "192.0.2.45",
        "event": "Repeated SSH login failures",
        "severity": "High",
        "count": 18,
    },
    {
        "timestamp": "2026-10-22 09:14:30",
        "source_ip": "198.51.100.23",
        "event": "Connection to decoy service",
        "severity": "Medium",
        "count": 1,
    },
    {
        "timestamp": "2026-10-22 09:18:02",
        "source_ip": "203.0.113.17",
        "event": "Port sweep against decoy host",
        "severity": "High",
        "count": 12,
    },
]

st.info(
    "Demo data only: these IP addresses are reserved for documentation "
    "and do not represent real attackers."
)

if st.button("Load Sample Events"):
    st.session_state["events"] = pd.DataFrame(sample_events)

uploaded = st.file_uploader("Upload event CSV (optional)", type=["csv"])
if uploaded:
    try:
        st.session_state["events"] = pd.read_csv(uploaded)
    except Exception as exc:
        st.error(f"Could not read CSV: {exc}")

if "events" in st.session_state:
    df = st.session_state["events"]
    st.subheader("Captured Events")
    st.dataframe(df, use_container_width=True)

    st.download_button(
        "Download Events CSV",
        data=df.to_csv(index=False).encode("utf-8"),
        file_name="honeynode_events.csv",
        mime="text/csv",
    )

    if st.button("Analyze Events with AI", type="primary"):
        if not api_key:
            st.warning("Enter your OpenAI API key in the sidebar.")
        else:
            with st.spinner("Reviewing event evidence..."):
                report = analyze_honeypot_events(api_key, df.to_dict("records"))
            st.subheader("AI Threat Assessment")
            st.markdown(report)
else:
    st.write("Select **Load Sample Events** or upload a CSV to begin.")

st.caption("Use only on systems and telemetry you are authorized to monitor.")
