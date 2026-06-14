from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Atlas Connection
MONGO_URI = "mongodb+srv://gwiraw_db_user:DEn4jRzi1b50iMVy@cluster0.dfy6y1w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["healthcare_survey"]
collection = db["participants"]

# Test connection
try:
    client.admin.command("ping")
    print("MongoDB Atlas Connected Successfully")
except Exception as e:
    print(e)

    # ==========================
    # HOME PAGE (ADD SURVEY)
    # ==========================
@app.route('/')
def home():
    return render_template('index.html')

# ==========================
# CREATE SURVEY
# ==========================
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

    return redirect('/surveys')

# ==========================
# READ ALL SURVEYS
# ==========================
@app.route('/surveys')
def surveys():
    try:
        records = list(collection.find())

        print("Records found:", len(records))

        return render_template(
    'surveys.html',
    records=records
)

    except Exception as e:
        return f"ERROR: {str(e)}"

# ==========================
# EDIT SURVEY
# ==========================
@app.route('/edit/<id>')
def edit(id):

    survey = collection.find_one(
        {"_id": ObjectId(id)}
    )

    return render_template(
'edit.html',
survey=survey
)

# ==========================
# UPDATE SURVEY
# ==========================
@app.route('/update/<id>', methods=['POST'])
def update(id):

    collection.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "age": int(request.form['age']),
                "gender": request.form['gender'],
                "income": float(request.form['income']),
                "utilities": float(request.form.get('utilities_amount') or 0),
                "entertainment": float(request.form.get('entertainment_amount') or 0),
                "schoolfees": float(request.form.get('schoolfees_amount') or 0),
                "shopping": float(request.form.get('shopping_amount') or 0),
                "healthcare": float(request.form.get('healthcare_amount') or 0)
            }
        }
    )

    return redirect('/surveys')

# ==========================
# DELETE SURVEY
# ==========================
@app.route('/delete/<id>')
def delete(id):

    collection.delete_one(
        {"_id": ObjectId(id)}
    )

    return redirect('/surveys')
# Elastic Beanstalk compatibility
application = app
# ==========================
# RUN APP
# ==========================
if __name__ == "__main__":
    app.run(debug=True)
 
