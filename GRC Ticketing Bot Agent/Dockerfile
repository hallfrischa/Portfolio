FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY grc_agent.py .
CMD ["sh", "-c", "while true; do python grc_agent.py; echo 'Sleeping for 5 minutes...'; sleep 300; done"]
