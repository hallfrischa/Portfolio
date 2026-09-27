# Consumer Security Risk Analytics (0-to-1 Portfolio)

**Objective:** Build a foundational data pipeline and analytics dashboard to detect consumer authentication risk, isolate device anomalies, and translate security telemetry into an actionable executive narrative.

This repository demonstrates a complete 0-to-1 security analytics lifecycle. It directly addresses the challenge of turning raw authentication data into a shared, trusted narrative that leadership, product partners, and security teams can act on.

##  Architecture & Projects

### 1. The Data Foundation (`/1_data_pipeline`)
*Building the shared data and pipelines required to evaluate consumer risk.*
*   **`generate_logs.py`**: A Python script simulating high-volume streaming authentication telemetry, deliberately injecting credential stuffing vectors and anomalous access patterns.
*   **`etl_pipeline.py`**: Normalizes unstructured JSON (parsing raw user-agents into device trust categories) and loads it into a highly queryable relational SQLite database.

### 2. Threat Hunting Analytics (`/2_threat_analytics`)
*Hands-on analytics to get to the root of consumer risk.*
*   **`threat_analytics.py`**: Terminal-based SQL execution script for rapid baseline health checks and automated anomaly detection.
*   **`Netflix_Auth_Threat_Hunt.ipynb`**: A Jupyter Notebook that executes advanced SQL anomaly detection to isolate botnet infrastructure, combining code, visualizations, and markdown to tell the data story.
*   **Key Signals Analyzed:** Authentication protocols (targeting legacy bypasses), failure rates, and device trust anomalies.

### 3. The Executive Dashboard (`/3_executive_dashboard`)
*Translating findings into a single, trusted narrative for security teams and leadership.*
*   **`dashboard.py`**: A Streamlit web application visualizing the ground-truth inventory of risk.
*   **Cost of Fraud Metric:** Quantifies active threats into estimated business loss to drive cross-functional alignment and prioritize mitigation strategies (e.g., rate-limiting legacy protocols).

## Quick Start
To run the executive dashboard locally:
```bash
git clone [https://github.com/hallfrischa/Portfolio.git](https://github.com/hallfrischa/Portfolio.git)
cd netflix-consumer-security-analytics
pip install -r requirements.txt
python 1_data_pipeline/generate_logs.py
python 1_data_pipeline/etl_pipeline.py
streamlit run 3_executive_dashboard/dashboard.py
