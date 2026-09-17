# Local LLM PII Sanitizer (AI DLP Proxy)

## Overview
A custom Data Loss Prevention (DLP) proxy script designed to act as a secure intermediary between users and artificial intelligence models. The script intercepts user prompts, scans them for sensitive data patterns such as Personally Identifiable Information (PII), and automatically redacts the sensitive data before the prompt is processed by the LLM.

## Business Value
* **Insider Threat Mitigation:** Prevents employees from inadvertently leaking sensitive corporate or customer data into AI tools.
* **Regulatory Compliance:** Enforces data privacy controls required by frameworks like GDPR, HIPAA, and PCI-DSS by ensuring unauthorized PII never enters the AI processing pipeline.
* **Zero-Trust AI Adoption:** Allows organizations to safely explore artificial intelligence capabilities while maintaining strict governance over data egress.

## Technologies Used
* **Python:** Core scripting and data handling.
* **Regular Expressions (Regex):** Pattern matching for identifying sensitive data structures (e.g., SSNs, credit card numbers, email addresses).
* **API Proxying:** Intercepting and manipulating data payloads in transit.

## Usage Instructions
1. Run the script: `python ai_security_proxy.py`
2. The proxy will listen for incoming prompt requests on the designated local port.
3. Configure your AI client to route requests through the proxy's IP and port instead of directly to the LLM.
4. The console will output a log of any redacted patterns whenever PII is detected and sanitized.