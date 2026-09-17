# AI Driven Vendor Risk Scorer

## Overview
A containerized, air-gapped web application designed to automate third-party risk assessments. This tool leverages a local Large Language Model (LLM) to evaluate vendor documentation—such as SOC 2 reports and privacy policies—and map potential security gaps against major compliance frameworks (e.g., NIST SP 800-171, GDPR). 

By keeping the LLM inference entirely local, this architecture ensures zero-trust data privacy, completely eliminating the risk of sensitive corporate data leaking to public cloud AI providers.

## Business Value
* **Accelerated Vendor Onboarding:** Automates the initial, time-consuming phase of reading and scoring lengthy compliance documentation.
* **Data Sovereignty:** Proves that AI can be leveraged for risk management without violating internal data loss prevention (DLP) policies.
* **Reproducible Infrastructure:** Containerized deployment ensures the application can be rapidly spun up in any environment.

## Technologies Used
* **Python:** Application logic and LLM API interfacing.
* **Streamlit:** Frontend web UI for intuitive file uploads and score readouts.
* **Docker:** Infrastructure containerization for isolated, reliable deployment.
* **Local LLM (Ollama):** Offline, private artificial intelligence inference.

## Deployment Instructions
1. Ensure a local LLM engine (like Ollama) is running and accessible.
2. Update the `LLM_API_URL` variable in `app.py` to point to your local LLM instance.
3. Build the container: `docker build -t vendor-risk-scorer:latest .`
4. Run the application: `docker run -d -p 8501:8501 vendor-risk-scorer:latest`
5. Access the web interface at `http://localhost:8501`.