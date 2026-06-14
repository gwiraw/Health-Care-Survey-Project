
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare_survey"]
collection = db["participants"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "age": int(request.form['age']),
        "gender": request.form['gender'],
        "income": float(request.form['income']),
        "utilities": float(request.form.get('utilities_amount') or 0),
        "entertainment": float(request.form.get('entertainment_amount') or 0),
        "schoolfees": float(request.form.get('schoolfees_amount') or 0),
        "shopping": float(request.form.get('shopping_amount') or 0),
        "healthcare": float(request.form.get('healthcare_amount') or 0)
    }

    collection.insert_one(data)
    return "Data submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
