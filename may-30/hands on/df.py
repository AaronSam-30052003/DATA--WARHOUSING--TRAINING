import pandas as pd
df=pd.read_csv("orders.csv")
print(df.head())
print(df.shape)
print(df.describe())
a=df.query("Status=='Delivered'")
print(a)
b=df['Status'].value_counts()
print(b)
df['Month']=pd.to_datetime(df['OrderDate']).dt.month
grouped=df.groupby(['Month','Status']).size().reset_index(name='Count')
print(grouped)
cols=['OrderID','CustomerName','Status']
subset=df[cols]
print(subset.head())

customer_info={
    1:"Madurai",
    2:"Kerala",
    3:"Bangalore",
    4:"Hyderabad"
}
df['City']=df['CustomerID'].map(customer_info)
print(df[['CustomerName','City']])

s=df.sort_values(by="TotalAmount",ascending=False)
print(s)

df.to_json("orders.json",orient="records",lines=True)

import numpy as np
c=np.array([1,2,3,4,5])
print(np.mean(c))
print(c*2)

data={
    'Name':['Aaron','sobana','Mickey','Choki'],
    'Marks':[70,100,90,95]
}
d=pd.DataFrame(data)
print(d)