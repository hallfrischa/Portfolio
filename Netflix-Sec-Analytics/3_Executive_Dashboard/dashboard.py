import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# --- Configuration & Setup ---
st.set_page_config(page_title="Consumer Security Risk Dashboard", layout="wide")
st.title("🛡️ Consumer Security Risk Portfolio")
st.markdown("Quarterly view of authentication anomalies, device trust, and estimated fraud impact.")

# Connect to the database we built in Project 1
conn = sqlite3.connect('security_warehouse.db')

# --- Metric 1: The Cost of Fraud ---
# Assuming every successful account takeover (ATO) costs the business $15 in support/refunds.
# We estimate ATOs by finding 'Success' logins from IPs that primarily generate 'Failures'.
cost_query = '''
SELECT COUNT(*) as ato_count FROM auth_events 
WHERE login_status = 'Success' AND ip_address IN (
    SELECT ip_address FROM auth_events 
    WHERE login_status = 'Failure_Bad_Password' GROUP BY ip_address HAVING COUNT(*) > 50
)
'''
ato_count = pd.read_sql(cost_query, conn).iloc[0]['ato_count']
estimated_loss = ato_count * 15.00

col1, col2, col3 = st.columns(3)
col1.metric(label="Detected Account Takeovers", value=f"{ato_count}")
col2.metric(label="Estimated Fraud Cost", value=f"${estimated_loss:,.2f}")
col3.metric(label="Active Botnet IPs", value="1")

st.divider()

# --- Visualization 1: Credential Stuffing Attack Vector ---
st.subheader("Credential Stuffing: Top Malicious IPs")
stuffing_query = '''
SELECT ip_address, COUNT(*) as failed_attempts, COUNT(DISTINCT user_id) as targeted_accounts
FROM auth_events WHERE login_status = 'Failure_Bad_Password'
GROUP BY ip_address HAVING failed_attempts > 50 ORDER BY failed_attempts DESC LIMIT 5
'''
df_stuffing = pd.read_sql(stuffing_query, conn)

fig_stuffing = px.bar(df_stuffing, x='ip_address', y='failed_attempts', 
                      hover_data=['targeted_accounts'], 
                      title="Failed Logins by IP Address",
                      labels={'failed_attempts': 'Failed Attempts', 'ip_address': 'IP Address'},
                      color_discrete_sequence=['#E50914']) # Netflix Red
st.plotly_chart(fig_stuffing, use_container_width=True)

# --- Visualization 2: Device Trust Anomalies ---
st.subheader("Device Trust: Failure Rates by Platform")
device_query = '''
SELECT device_type, 
       COUNT(*) as total, 
       SUM(CASE WHEN login_status = 'Failure_Bad_Password' THEN 1 ELSE 0 END) as failures
FROM auth_events GROUP BY device_type
'''
df_device = pd.read_sql(device_query, conn)
df_device['failure_rate'] = (df_device['failures'] / df_device['total']) * 100

fig_device = px.bar(df_device, x='device_type', y='failure_rate',
                    title="Authentication Failure Rate by Device Type (%)",
                    labels={'failure_rate': 'Failure Rate (%)', 'device_type': 'Device Category'})
st.plotly_chart(fig_device, use_container_width=True)

conn.close()