"""
Enterprise AI Security Proxy & DLP Engine
Author: MSCSIA IT & Security Professional
Description: 
A lightweight Data Loss Prevention (DLP) middleware script designed to intercept 
outbound prompts to public Large Language Models (LLMs). It utilizes regular 
expressions to detect and redact Personally Identifiable Information (PII) 
and hardcoded secrets before transmission.
"""

import re
import logging
import json
from typing import Dict, List, Tuple

# Configure audit logging for security monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [SECURITY_PROXY] - %(levelname)s - %(message)s'
)

class AISecurityProxy:
    def __init__(self):
        # Define DLP Regular Expression Patterns for data sanitization
        self.dlp_patterns = {
            "PII_SSN": r"\b\d{3}[-.]?\d{2}[-.]?\d{4}\b",
            "PII_CREDIT_CARD": r"\b(?:\d[ -]*?){13,16}\b",
            "CRED_API_KEY": r"(?i)(?:api_key|secret|token|password)[\s:=]+[\'\"]?[a-zA-Z0-9_\-]{16,64}[\'\"]?",
            "CRED_AWS_KEY": r"(?i)AKIA[0-9A-Z]{16}",
            "IP_INTERNAL_DOMAIN": r"\b[a-zA-Z0-9.-]+\.internal\.corp\b"
        }

    def scan_prompt(self, prompt: str) -> Tuple[bool, List[str]]:
        """
        Scans the prompt against predefined DLP patterns.
        Returns a boolean indicating if a threat was found, and a list of triggered rules.
        """
        triggered_rules = []
        for rule_name, pattern in self.dlp_patterns.items():
            if re.search(pattern, prompt):
                triggered_rules.append(rule_name)
                
        is_flagged = len(triggered_rules) > 0
        return is_flagged, triggered_rules

    def redact_prompt(self, prompt: str) -> str:
        """
        Replaces sensitive matched data with a standardized [REDACTED] tag.
        """
        sanitized_prompt = prompt
        for rule_name, pattern in self.dlp_patterns.items():
            # Replace the sensitive match with the name of the rule that caught it
            redaction_tag = f"[REDACTED: {rule_name}]"
            sanitized_prompt = re.sub(pattern, redaction_tag, sanitized_prompt)
            
        return sanitized_prompt

    def process_outbound_request(self, user_id: str, raw_prompt: str) -> Dict[str, str]:
        """
        Main proxy function to process, log, and sanitize outbound LLM requests.
        """
        logging.info(f"Analyzing outbound prompt from User: {user_id}")
        
        is_flagged, triggered_rules = self.scan_prompt(raw_prompt)
        
        if is_flagged:
            logging.warning(f"DLP Alert! User {user_id} attempted to send sensitive data. Rules triggered: {triggered_rules}")
            sanitized_prompt = self.redact_prompt(raw_prompt)
            logging.info("Prompt successfully sanitized. Proceeding to LLM endpoint.")
            
            return {
                "status": "sanitized",
                "original_length": len(raw_prompt),
                "safe_prompt": sanitized_prompt
            }
            
        logging.info("Prompt passed DLP checks. No sensitive data detected.")
        return {
            "status": "clean",
            "original_length": len(raw_prompt),
            "safe_prompt": raw_prompt
        }

# ==========================================
# Execution Block: Demonstration for Portfolio
# ==========================================
if __name__ == "__main__":
    # Initialize the Security Proxy
    proxy = AISecurityProxy()

    # Mock user prompt containing simulated sensitive data
    test_prompt = (
        "Can you help me format this configuration file? "
        "The database admin password is db_password = 'super_secret_token_89237498237' "
        "and my AWS key is AKIA1234567890EXAMPLE. "
        "Also, ping the server at database.internal.corp to check the connection."
    )

    print("--- RAW PROMPT (PENDING TRANSMISSION) ---")
    print(test_prompt)
    print("\n--- INITIATING SECURITY PROXY SCAN ---")
    
    # Process the prompt through the middleware
    result = proxy.process_outbound_request(user_id="admin_01", raw_prompt=test_prompt)
    
    print("\n--- FINAL SANITIZED PROMPT (SENT TO LLM) ---")
    print(result["safe_prompt"])
    print("\nProxy Execution Completed.")