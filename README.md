
# Healthcare Survey Project

## Overview
Flask application that collects participant data, stores it in MongoDB, exports data to CSV, and analyzes spending patterns using Jupyter Notebook.

## Technologies
- Flask
- MongoDB
- Python
- Pandas
- Matplotlib
- Jupyter
- AWS EC2

## Run Application
pip install -r requirements.txt

python app.py

## Export Data
python export_csv.py

## Notebook
Open notebooks/analysis.ipynb and run all cells.

## AWS Deployment
Deploy on AWS EC2 and run using:
gunicorn app:app
