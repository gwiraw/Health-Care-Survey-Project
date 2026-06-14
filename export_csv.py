
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare_survey"]
collection = db["participants"]

records = list(collection.find())

for record in records:
    record.pop("_id", None)

df = pd.DataFrame(records)
df.to_csv("data/survey_data.csv", index=False)

print("CSV exported successfully.")
