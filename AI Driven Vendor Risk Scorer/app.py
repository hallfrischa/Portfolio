import streamlit as st
import requests
import PyPDF2

# Configure your Unraid offline LLM endpoint (Using Ollama's native API)
LLM_API_URL = "http://Ollama's_IP:11434/api/chat" # Change IP address
LLM_MODEL = "llava" # Update if you are running a different model locally

st.set_page_config(page_title="Vendor Risk Scorer", layout="wide")
st.title("Agentic Vendor Risk & Compliance Scorer")

uploaded_file = st.file_uploader("Upload Vendor Policy or SOC Report (PDF)", type="pdf")

if uploaded_file is not None:
    # 1. Extract Text from PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    document_text = ""
    for page in pdf_reader.pages:
        document_text += page.extract_text() + "\n"
        
    st.info(f"Successfully extracted {len(document_text)} characters from document.")
    
    if st.button("Run Governance Audit"):
        with st.spinner("Analyzing against compliance frameworks..."):
            
            # 2. Structure the GRC Prompt
            system_prompt = """You are an expert Third-Party Risk Analyst. 
            Evaluate the provided vendor security document against NIST SP 800-171, SOC 2, and GDPR requirements.
            
            Provide your output in Markdown using this exact structure:
            * **Overall Risk Score:** (Low, Medium, or High)
            * **Data Protection & Encryption:** (Status and gaps)
            * **Access Control & Identity:** (Status and gaps)
            * **Incident Response & SLA:** (Status and gaps)
            * **Red Flags:** (List any critical missing clauses)
            """
            
            # 3. Update payload for Ollama's native format
            payload = {
                "model": LLM_MODEL,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    # Truncate text to prevent overflowing the model's context window
                    {"role": "user", "content": f"Document Text:\n\n{document_text[:5000]}"} 
                ],
                "stream": False, # Tells Ollama to wait and send one complete response
                "options": {
                    "temperature": 0.1 # Low temperature for analytical strictness
                }
            }
            
            # 4. Call the Local LLM
            try:
                response = requests.post(LLM_API_URL, json=payload)
                response.raise_for_status()
                
                # Parse Ollama's native JSON structure
                evaluation = response.json()['message']['content']
                
                st.subheader("Audit Results")
                st.markdown(evaluation)
                
            except Exception as e:
                st.error(f"Failed to connect to local LLM: {e}")