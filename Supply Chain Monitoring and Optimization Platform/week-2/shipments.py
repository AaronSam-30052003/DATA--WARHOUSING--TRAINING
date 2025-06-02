from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["supply_chain"]
shipments = db["shipments"]

# Insert multiple shipment documents
shipment_data = [
    {"shipment_id": "S101", "order_id": 1, "status": "In Transit", "timestamp": datetime.now()},
    {"shipment_id": "S102", "order_id": 2, "status": "Delivered", "timestamp": datetime.now()},
    {"shipment_id": "S103", "order_id": 3, "status": "Delayed", "timestamp": datetime.now()},
    {"shipment_id": "S104", "order_id": 4, "status": "Pending", "timestamp": datetime.now()},
    {"shipment_id": "S105", "order_id": 5, "status": "Delivered", "timestamp": datetime.now()},
    {"shipment_id": "S106", "order_id": 6, "status": "In Transit", "timestamp": datetime.now()},
    {"shipment_id": "S107", "order_id": 7, "status": "Out for Delivery", "timestamp": datetime.now()}
]

result = shipments.insert_many(shipment_data)
print(f"Inserted IDs: {result.inserted_ids}")
