import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('customer_orders.csv')
df.columns = df.columns.str.strip().str.lower()

# Convert timestamps
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['delivery_date'] = pd.to_datetime(df['delivery_date'], errors='coerce')
df['submitted_at'] = pd.to_datetime(df['submitted_at'], errors='coerce')

# Fill missing delivery dates
df['delivery_date'] = df['delivery_date'].fillna(pd.Timestamp.today())

# Calculate delivery delays using NumPy
df['delay_days'] = (df['delivery_date'] - df['order_date']).dt.days
df['delayed'] = np.where(df['delay_days'] > 3, 1, 0)  # Threshold = 3 days

# Top delayed customers
top_delayed = df.groupby('customer_id')['delayed'].sum().sort_values(ascending=False)
print("\n Top 5 Delayed Customers:")
print(top_delayed.head(5))

# Most common feedback issues
if 'feedback' in df.columns:
    issues = (
        df['feedback']
        .dropna()
        .str.lower()
        .str.extractall(r'([a-z]+)')[0]
        .value_counts()
        .head(10)
    )
    print("\n Most Common Words in Feedback Issues:")
    print(issues)
else:
    print("\n No 'feedback' column available.")

# Save the preprocessed dataset
df.to_csv('preprocessed_customer_orders.csv', index=False)

