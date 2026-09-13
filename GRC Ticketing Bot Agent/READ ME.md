# GRC Ticketing Bot Agent

## Overview
An automated background agent that continuously integrates an IT Service Management (ITSM) platform with a local, private Large Language Model. The bot polls the Zammad API for newly created support tickets, evaluates the user requests for potential policy violations or security risks, and seamlessly injects a GRC assessment score directly into the ticket as an internal note.

## Business Value
* **Proactive Risk Identification:** Flags potential issues like Shadow IT, unauthorized access requests, or data exfiltration attempts before IT staff begin fulfillment.
* **Workflow Automation:** Operates continuously in a lightweight container, reducing the manual triage burden on compliance analysts.
* **Secure API Integration:** Demonstrates programmatic interaction with enterprise ticketing systems while maintaining strict internal data privacy.

## Technologies Used
* **Python:** Core automation logic and API request handling.
* **Zammad API:** Interfacing with the ITSM platform for ticket retrieval and note injection.
* **Docker:** Deployed as a headless, continuous background service utilizing a controlled execution loop to optimize resource utilization.
* **Local LLM (Ollama):** Offline risk analysis ensuring ticket data never leaves the internal network.

## Deployment Instructions
1. Generate an API token within your Zammad instance.
2. Update the `zammad_host`, `api_token`, and `llm_api_url` variables within `grc_agent.py` to match your internal environment.
3. Build the container: `docker build -t grc-ticketing-bot-agent:latest .`
4. Deploy the background agent: `docker run -d --restart unless-stopped --name GRC-Ticketing-Bot-Agent grc-ticketing-bot-agent:latest`