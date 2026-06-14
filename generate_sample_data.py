from pymongo import MongoClient
import random

MONGO_URI = "mongodb+srv://gwiraw_db_user:DEn4jRzi1b50iMVy@cluster0.dfy6y1w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["healthcare_survey"]
collection = db["participants"]

client.admin.command("ping")
print("MongoDB Atlas Connected Successfully")

records = []

for _ in range(200):
    records.append({
        "age": random.randint(18, 70),
        "gender": random.choice(["Male", "Female"]),
        "income": random.randint(500, 7000),
        "utilities": random.randint(50, 600),
        "entertainment": random.randint(20, 400),
        "schoolfees": random.randint(0, 1500),
        "shopping": random.randint(50, 1000),
        "healthcare": random.randint(20, 500)
    })

result = collection.insert_many(records)

print(f"Inserted {len(result.inserted_ids)} records")
print(f"Total records in collection: {collection.count_documents({})}")

