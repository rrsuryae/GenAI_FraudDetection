from google.cloud import bigquery

def get_user_behavior_summary(customer_id, days=30):
    client = bigquery.Client()
    query = f"""
        SELECT location, device, COUNT(*) AS txn_count
        FROM `your-project-id.banking.transactions`
        WHERE customer_id = '{customer_id}' AND timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL {days} DAY)
        GROUP BY location, device
        ORDER BY txn_count DESC
        LIMIT 5
    """
    results = client.query(query).to_dataframe()
    if results.empty:
        return "No recent behavior found."
    return "; ".join([
        f"{row['txn_count']} transactions from {row['location']} on {row['device']}"
        for _, row in results.iterrows()
    ])
