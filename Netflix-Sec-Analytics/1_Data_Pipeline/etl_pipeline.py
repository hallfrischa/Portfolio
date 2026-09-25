import json
import sqlite3

# 1. SETUP: Connect to the database and define the schema (The Data Model)
DB_NAME = 'security_warehouse.db'
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Dropping table if it exists to allow for easy re-runs during development
cursor.execute('DROP TABLE IF EXISTS auth_events')

# Building the schema
cursor.execute('''
CREATE TABLE auth_events (
    event_id TEXT PRIMARY KEY,
    event_timestamp DATETIME,
    user_id TEXT,
    ip_address TEXT,
    device_type TEXT,
    auth_protocol TEXT,
    login_status TEXT
)
''')
conn.commit()

# 2. TRANSFORM: Function to clean and categorize raw data
def categorize_device(user_agent):
    if "iPhone" in user_agent or "Android" in user_agent:
        return "Mobile"
    elif "Roku" in user_agent or "SmartTV" in user_agent:
        return "Smart TV"
    elif "Windows" in user_agent or "Macintosh" in user_agent:
        return "Desktop"
    else:
        return "Unknown/Other"

# 3. EXTRACT & LOAD: Read the JSON file and insert into SQL
def main():
    records_to_insert = []
    
    print("Extracting and transforming logs...")
    with open('auth_logs.json', 'r') as file:
        for line in file:
            log = json.loads(line)
            
            # Apply transformation
            device_type = categorize_device(log['user_agent'])
            
            # Structure the record for SQL insertion
            records_to_insert.append((
                log['event_id'],
                log['timestamp'],
                log['user_id'],
                log['ip_address'],
                device_type,
                log['auth_protocol'],
                log['status']
            ))

    print(f"Loading {len(records_to_insert)} records into {DB_NAME}...")
    
    # Bulk insert is much faster than row-by-row
    cursor.executemany('''
    INSERT INTO auth_events 
    (event_id, event_timestamp, user_id, ip_address, device_type, auth_protocol, login_status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', records_to_insert)

    conn.commit()
    conn.close()
    print("ETL Pipeline completed successfully! Data is structured and ready for analysis.")

if __name__ == "__main__":
    main()