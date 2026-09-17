from zammad_py import ZammadAPI
import requests

# 1. Connect to your Unraid Zammad instance
zammad_host = 'http://YOUR-ZAMMAD-IP/api/v1/'
api_token = 'YOUR_GENERATED_TOKEN'
client = ZammadAPI(url=zammad_host, http_token=api_token)

# Configure your Unraid offline LLM endpoint (Ollama Native API)
llm_api_url = "http://URL:11434/api/chat"
llm_model = "llava" # The model currently loaded on your Unraid server

# 2. Fetch all newly created tickets dynamically
print("Scanning Zammad for new tickets...")
# Queries Zammad for any ticket currently in the "new" state
new_tickets = client.ticket.search(query="state:new")

if not new_tickets:
    print("No new tickets found. Exiting.")

# Loop through every new ticket found
for ticket in new_tickets:
    ticket_id = ticket['id']
    ticket_body = ticket['title'] # You can also fetch ticket['article'] for full body text
    
    print(f"\nEvaluating Ticket #{ticket_id}: {ticket_body}")

    # 3. Send to LLM for GRC Evaluation
    system_prompt = """You are a strict Corporate Governance, Risk, and Compliance (GRC) Agent. 
    Review the user's IT request. 
    1. Assign a Risk Score: LOW, MEDIUM, or HIGH.
    2. Identify any potential policy violations (e.g., Data Exfiltration, Shadow IT, Unauthorized Access).
    3. Provide a brief recommendation for the IT staff.
    Keep your response concise and formatted in Markdown."""

    # Updated payload for Ollama's native format
    payload = {
        "model": llm_model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Ticket Request: {ticket_body}"}
        ],
        "stream": False,
        "options": {
            "temperature": 0.1
        }
    }

    try:
        print("Sending to local LLM...")
        response = requests.post(llm_api_url, json=payload)
        response.raise_for_status()
        
        # Parse Ollama's native JSON structure
        llm_evaluation = response.json()['message']['content']
        print("LLM assessment generated successfully.")
        
    except Exception as e:
        print(f"LLM Connection Error on Ticket #{ticket_id}: {e}")
        llm_evaluation = "**GRC Agent Offline:** Unable to reach the local LLM engine for risk assessment."

    # 4. Inject the LLM assessment as an Internal Note back into Zammad
    note_params = {
        "ticket_id": ticket_id,
        "subject": "Automated GRC AI Assessment",
        "body": llm_evaluation,
        "type": "note",
        "internal": True, # Ensures the end-user doesn't see the bot's risk score
        "content_type": "text/html"
    }

    # Push the note to the ticket
    client.ticket_article.create(params=note_params)
    print(f"Governance note successfully added to Ticket #{ticket_id}.")