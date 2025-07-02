import pandas as pd
df = pd.read_csv('Data/cleaned_delayed_orders.csv')
delayed_orders = df[df['is_delayed'] == 1]
summary = delayed_orders.groupby('supplierid').size().reset_index(name='delayed_count')
summary.to_csv('Data/delayed_summary.csv', index=False)
print("Processed summary saved.")
print(summary)
