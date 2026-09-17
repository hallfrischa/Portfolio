import streamlit as st
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine

# Cache the heavy NLP models so the app doesn't reload them on every button click
@st.cache_resource
def load_engines():
    return AnalyzerEngine(), AnonymizerEngine()

analyzer, anonymizer = load_engines()

st.title("🛡️ Enterprise PII Sanitizer Pipeline")
st.write("Intercept, detect, and redact sensitive data payloads prior to LLM transmission.")

raw_text = st.text_area(
    "Input Raw Prompt / Data:", 
    height=200, 
    placeholder="e.g., Contact John Doe at 555-0199 regarding the Microsoft audit..."
)

if st.button("Sanitize Payload"):
    if raw_text:
        # 1. Analyze text for all supported PII entities
        results = analyzer.analyze(text=raw_text, entities=[], language='en')
        
        # 2. Anonymize the text based on findings
        anonymized_result = anonymizer.anonymize(text=raw_text, analyzer_results=results)
        
        st.write("**Sanitized Output (Safe for LLM Processing):**")
        st.code(anonymized_result.text, language="text")
        
        # 3. Output the audit trail for GRC logging
        with st.expander("View Governance Audit Log"):
            if results:
                for res in results:
                    st.write(f"- **Flagged:** `{res.entity_type}` | **Confidence:** `{res.score:.2f}`")
            else:
                st.write("No PII detected.")
    else:
        st.warning("Please enter a text payload to sanitize.")