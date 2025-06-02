import pyodbc
import pandas as pd
import numpy as np

# Connect to your local SQL Server
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-EDPEQIQ\SQLEXPRESS;'  
    'DATABASE=SupplyChain;'
    'Trusted_Connection=yes;'
)

# SQL query joining all required tables
query = """
SELECT 
    o.OrderID, 
    o.SupplierID,
    s.Name AS SupplierName,
    i.ItemID,
    i.ItemName,
    o.OrderDate,
    o.DeliveryDate
FROM supply.Orders o
JOIN supply.Suppliers s ON o.SupplierID = s.SupplierID
JOIN supply.Inventory i ON o.ItemID = i.ItemID;
"""

# Load into DataFrame
df = pd.read_sql(query, conn)
# Ensure datetime format
df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'])
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
# Calculate delay_days from today and mark delay
df['delay_days'] = (pd.Timestamp.today() - df['DeliveryDate']).dt.days
df['is_delayed'] = np.where(df['delay_days'] > 0, 1, 0)
# Show result
print(df[['OrderID', 'SupplierName', 'ItemName', 'DeliveryDate', 'delay_days', 'is_delayed']])
# Save to CSV
df.to_csv("SupplyChain_Delivery_Report.csv", index=False)
print("SupplyChain_Delivery_Report.csv")
