import sqlite3

def run_query(cursor, query_name, query):
    print(f"\n--- {query_name} ---")
    cursor.execute(query)
    columns = [description[0] for description in cursor.description]
    results = cursor.fetchall()
    
    # Basic formatting for the terminal output
    print(f"{columns[0]:<20} | {columns[1]:<20} | {columns[2] if len(columns) > 2 else ''}")
    print("-" * 60)
    for row in results:
        print(f"{str(row[0]):<20} | {str(row[1]):<20} | {str(row[2]) if len(row) > 2 else ''}")

def main():
    conn = sqlite3.connect('security_warehouse.db')
    cursor = conn.cursor()

    # Query 1: Platform-wide Authentication Health
    # What is the baseline failure rate? If this spikes, we have a platform-wide attack.
    q1 = '''
    SELECT 
        login_status, 
        COUNT(*) as event_count,
        ROUND((COUNT(*) * 100.0 / (SELECT COUNT(*) FROM auth_events)), 2) as percentage
    FROM auth_events
    GROUP BY login_status
    ORDER BY event_count DESC;
    '''
    run_query(cursor, "Platform-wide Auth Health", q1)

    # Query 2: Credential Stuffing Detection
    # Find IP addresses that have a massive number of failed logins across MANY different user accounts.
    q2 = '''
    SELECT 
        ip_address, 
        COUNT(*) as failed_attempts,
        COUNT(DISTINCT user_id) as unique_accounts_targeted
    FROM auth_events
    WHERE login_status = 'Failure_Bad_Password'
    GROUP BY ip_address
    HAVING failed_attempts > 50
    ORDER BY failed_attempts DESC
    LIMIT 5;
    '''
    run_query(cursor, "Credential Stuffing Detection", q2)

    # Query 3: Device Trust Anomalies
    # Attackers often use automated scripts (like Python requests) which show up as "Unknown/Other" device types.
    q3 = '''
    SELECT 
        device_type, 
        COUNT(*) as total_logins,
        SUM(CASE WHEN login_status = 'Failure_Bad_Password' THEN 1 ELSE 0 END) as total_failures
    FROM auth_events
    GROUP BY device_type
    ORDER BY total_failures DESC;
    '''
    run_query(cursor, "Device Trust & Failure Correlation", q3)

    conn.close()

if __name__ == "__main__":
    main()