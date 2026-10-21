import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain

def analyze_honeypot_telemetry(api_key, telemetry_data):
    if not api_key:
        return "Error: OpenAI API Key is missing."
    
    os.environ["OPENAI_API_KEY"] = api_key
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    
    prompt = PromptTemplate(
        input_variables=["telemetry"],
        template="""
You are an expert Threat Intelligence Analyst and Deception Operations Specialist.
Analyze the following honeypot interaction logs and attacker interaction telemetry:

HONEYPOT TELEMETRY:
{telemetry}

Provide a comprehensive Attacker Profile & Threat Capture Report containing:
1. **Attacker Classification & Threat Level (Low / Medium / High / Critical)**
2. **Inferred Threat Actor Intent & Tools (e.g., Automated Scanner, Human Recon, Worm)**
3. **MITRE ATT&CK Tactics & Techniques Mapping (with IDs)**
4. **Countermeasure & Deception Hardening Strategy**
        """
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(telemetry=telemetry_data)
