#using request
import pandas as pd
import numpy as np
import requests
# Fetch sample data from a placeholder API
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data=response.json()
# Convert JSON data to DataFrame
df = pd.DataFrame(data)
# Simulate relevant columns for the example
import random
from datetime import datetime, timedelta
np.random.seed(42)
# Create fake delivery_date within last 30 days
df['delivery_date'] = [datetime.today() - timedelta(days=random.randint(0, 40)) for _ in range(len(df))]
df['order_id'] = df['id']
df['supplier_id'] = np.random.randint(1000, 1020, size=len(df))
# Convert 'delivery_date' to datetime
df['delivery_date'] = pd.to_datetime(df['delivery_date'])
# Calculate delay_days (how many days since delivery_date compared to today)
df['delay_days'] = (pd.Timestamp.today() - df['delivery_date']).dt.days
# Mark delayed if delay_days > 0
df['is_delayed'] = np.where(df['delay_days'] > 0, 1, 0)
# Display cleaned and processed data
print(df[['order_id', 'supplier_id', 'delivery_date', 'delay_days', 'is_delayed']].head(10))
#Save the preprocessed order into csv
df.to_csv("processed_orders.csv", index=False)

#using pandas to load the data
import pandas as pd
import numpy as np
# Load from local CSV
df = pd.read_csv('SupplyChain_Delivery_Report.csv')
# Normalize column names
df.columns = df.columns.str.strip().str.lower()
# Clean data using pandas
# Drop rows with all null values
df.dropna(how='all', inplace=True)
# Show missing data summary
print("\nMissing values per column:\n", df.isnull().sum())
# Format relevant date columns
date_cols = [col for col in df.columns if 'date' in col]
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')
# Drop rows where essential dates are missing
df.dropna(subset=['orderdate', 'deliverydate'], inplace=True)
# Perform basic calculations using NumPy
# Calculate delivery delay
df['delay_days'] = (df['deliverydate'] - df['orderdate']).dt.days
df['delayed'] = np.where(df['delay_days'] > 3, 1, 0)

# Simulate stock calculation (if stock columns exist)
if 'quantity ordered' in df.columns and 'quantity delivered' in df.columns:
    df['shortage'] = np.where(
        df['quantity delivered'] < df['quantity ordered'],
        df['quantity ordered'] - df['quantity delivered'],
        0
    )

# Display cleaned and processed data
print("\n Cleaned and Processed Data Preview:")
print(df.head())

# Save processed data to new CSV
df.to_csv('processed_supply_chain_report.csv', index=False)
print("\n processed_supply_chain_report.csv")

