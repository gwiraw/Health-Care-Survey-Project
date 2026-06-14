# Health Care Survey Management System

## Project Overview

The Health Care Survey Management System is a cloud-based web application developed using Flask, MongoDB Atlas, AWS Elastic Beanstalk, and Python Data Analytics libraries. The system enables users to collect, manage, analyze, and visualize healthcare-related household expenditure data.

The application supports full CRUD (Create, Read, Update, Delete) functionality for survey records and integrates with MongoDB Atlas for cloud database storage. Data collected can be exported for analysis and visualized using Python libraries such as Pandas and Matplotlib.

This project was developed as part of a Master's Degree in Data Analytics to demonstrate competencies in:

* Web Application Development
* NoSQL Databases
* Cloud Computing
* Data Analytics
* Data Visualization
* AWS Deployment

---

# Features

## Survey Data Collection

Users can submit survey information including:

* Age
* Gender
* Monthly Income
* Utilities Expenditure
* Entertainment Expenditure
* School Fees Expenditure
* Shopping Expenditure
* Healthcare Expenditure

---

## CRUD Operations

The system provides complete CRUD functionality:

### Create

Add new survey records through a web form.

### Read

View all survey records in a searchable dashboard.

### Update

Edit existing survey records.

### Delete

Remove survey records from the database.

---

## Data Storage

Survey records are stored in MongoDB Atlas, a cloud-hosted NoSQL database.

### Database

Database Name:

```text
healthcare_survey
```

Collection Name:

```text
participants
```

---

## Data Analytics

The project includes Jupyter Notebook analysis using:

* Pandas
* NumPy
* Matplotlib

Analysis includes:

* Average Income by Age
* Gender Distribution
* Spending Category Analysis
* Healthcare Expenditure Trends

---

## Data Visualization

Visualizations generated include:

### Average Income by Age

Illustrates income distribution across age groups.

### Gender Distribution Against Spending Categories

Shows spending behaviour patterns by gender.

Generated charts are stored in:

```text
charts/
```

---

## Cloud Deployment

The application is deployed on AWS Elastic Beanstalk.

Services used:

* AWS Elastic Beanstalk
* Amazon EC2
* Amazon S3
* Application Load Balancer

---

# System Architecture

```text
User Browser
      |
      v
Flask Web Application
      |
      v
MongoDB Atlas Database
      |
      v
Data Analytics Layer
(Pandas + Matplotlib)
      |
      v
Reports & Visualizations
```

---

# Technologies Used

## Backend

* Python 3.13
* Flask

## Database

* MongoDB Atlas
* PyMongo

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

## Analytics

* Pandas
* NumPy
* Matplotlib

## Cloud

* AWS Elastic Beanstalk
* Amazon EC2
* Amazon S3

## Version Control

* Git
* GitHub

---

# Project Structure

```text
Health-Care-Survey-Project
│
├── app.py
├── export_csv.py
├── generate_sample_data.py(To boost the sample for analysis after manual entry)
├── requirements.txt
├── Procfile
├── README.md
│
├── data/
│   └── survey_data.csv
│
├── charts/
│   ├── age_income.png
│   └── gender_spending.png
│
├── notebooks/
│   └── analysis.ipynb
│
├── static/
│   └── logo.png
│
├── templates/
│   ├── index.html
│   ├── surveys.html
│   └── edit.html
│
└── venv/
```

---

# Installation Guide

## Clone Repository

```bash
git clone https://github.com/gwiraw/Health-Care-Survey-Project.git
```

```bash
cd Health-Care-Survey-Project
```

---

## Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# MongoDB Configuration

Create a MongoDB Atlas Cluster.

Create a database user.

Add IP Access:

```text
0.0.0.0/0
```

Update MongoDB URI inside:

```python
app.py
```

Example:

```python
MONGO_URI = "mongodb+srv://username:password@cluster.mongodb.net/?retryWrites=true&w=majority"
```

---

# Running Locally

Start Flask:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# Generating Sample Data

Generate 200 sample records:

```bash
python generate_sample_data.py
```

---

# Export Data

Export survey data to CSV:

```bash
python export_csv.py
```

Output:

```text
data/survey_data.csv
```

---

# Data Analysis

Open Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/analysis.ipynb
```

Run all cells to:

* Clean data
* Analyze trends
* Generate charts

---

# AWS Deployment

## Initialize Elastic Beanstalk

```bash
eb init
```

Select:

```text
Python 3.13 running on 64bit Amazon Linux 2023
```

---

## Create Environment

```bash
eb create healthcare-env
```

---

## Deploy Updates

```bash
eb deploy
```

---

## Check Environment Status

```bash
eb status
```

```bash
eb health
```

---

# Live Application

Application URL:

```text
http://healthcare-env.eba-hr3bhdtq.us-east-1.elasticbeanstalk.com
```

---

# Challenges Encountered

During deployment several technical challenges were encountered:

## AWS Credential Authentication Issues

Resolved by:

* Creating IAM User
* Generating Access Keys
* Configuring AWS CLI

---

## Elastic Beanstalk Procfile Configuration

Resolved by:

```python
application = app
```

and

```text
web: gunicorn app:app
```

---

## Dependency Installation Errors

Resolved by removing Windows-specific packages from:

```text
requirements.txt
```

Examples removed:

* pywin32
* pypiwin32
* pythonnet

---

## MongoDB Atlas Connectivity

Resolved by:

Adding:

```text
0.0.0.0/0
```

to MongoDB Atlas Network Access List.

---

# Future Improvements

Potential enhancements include:

* User Authentication
* Role-Based Access Control
* Dashboard Analytics
* Predictive Healthcare Models
* Automated Reporting
* Power BI Integration
* Mobile Responsive Design
* API Development

---

# Learning Outcomes

This project demonstrates practical skills in:

* Full Stack Development
* Cloud Deployment
* NoSQL Database Management
* Data Visualization
* Data Analytics
* AWS Infrastructure
* Python Programming

---

# Author

Wadzanai Gwira

Master of Science in Data Analytics 

2026

---

# License

This project is developed for educational and research purposes.

© 2026 Wadzanai Gwira. All Rights Reserved.
