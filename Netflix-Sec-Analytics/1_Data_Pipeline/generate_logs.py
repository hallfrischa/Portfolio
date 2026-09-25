import json
import random
import uuid
from datetime import datetime, timedelta

# Configuration
NUM_NORMAL_LOGINS = 8000
NUM_ATTACK_LOGINS = 2000
OUTPUT_FILE = "auth_logs.json"

# Reference Data
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36", # Web
    "Netflix/7.104.0 (iPhone; iOS 14.4; Scale/2.00)",               # Mobile App
    "Roku/DVP-9.10 (9.10.00.4111-46)",                              # Smart TV
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"            # Unknown/Linux
]
AUTH_PROTOCOLS = ["OAuth2", "SAML", "Basic_Auth"]
STATUSES = ["Success", "Failure_Bad_Password", "MFA_Challenge_Issued"]

def generate_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def main():
    logs = []
    base_time = datetime.now() - timedelta(days=7)

    # 1. Generate Normal Traffic
    print(f"Generating {NUM_NORMAL_LOGINS} normal login events...")
    for _ in range(NUM_NORMAL_LOGINS):
        logs.append({
            "event_id": str(uuid.uuid4()),
            "timestamp": (base_time + timedelta(minutes=random.randint(1, 10000))).isoformat(),
            "user_id": f"user_{random.randint(1000, 9999)}",
            "ip_address": generate_ip(),
            "user_agent": random.choices(USER_AGENTS, weights=[40, 40, 15, 5])[0],
            "auth_protocol": random.choices(AUTH_PROTOCOLS, weights=[70, 20, 10])[0],
            "status": random.choices(STATUSES, weights=[85, 10, 5])[0]
        })

    # 2. Inject a "Credential Stuffing" Attack (1 IP hitting many accounts rapidly)
    print(f"Injecting {NUM_ATTACK_LOGINS} credential stuffing events...")
    attacker_ip = "192.168.1.100" # Static IP for the attack
    attack_time = base_time + timedelta(days=2)
    
    for _ in range(NUM_ATTACK_LOGINS):
        attack_time += timedelta(seconds=random.randint(1, 5)) # Rapid fire
        logs.append({
            "event_id": str(uuid.uuid4()),
            "timestamp": attack_time.isoformat(),
            "user_id": f"user_{random.randint(1000, 9999)}", # Guessing random users
            "ip_address": attacker_ip,
            "user_agent": USER_AGENTS[3], # Using a Linux/Unknown agent
            "auth_protocol": "Basic_Auth", # Legacy protocol target
            "status": "Failure_Bad_Password" # Mostly failing
        })

    # Sort logs chronologically to simulate a real log stream
    logs.sort(key=lambda x: x["timestamp"])

    # 3. Export to JSON
    with open(OUTPUT_FILE, 'w') as f:
        for log in logs:
            f.write(json.dumps(log) + "\n")
            
    print(f"Success! {len(logs)} log events written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()