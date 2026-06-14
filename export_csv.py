from pymongo import MongoClient
import pandas as pd

MONGO_URI = "mongodb+srv://gwiraw_db_user:DEn4jRzi1b50iMVy@cluster0.dfy6y1w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["healthcare_survey"]
collection = db["participants"]

records = list(collection.find())

for record in records:
    record.pop("_id", None)

    df = pd.DataFrame(records)

    df.to_csv("data/survey_data.csv", index=False)

    print("CSV exported successfully!")
    print(df.head())