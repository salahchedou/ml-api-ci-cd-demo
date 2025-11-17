1. Project Overview

This project demonstrates how to:

Build a small API using FastAPI

Serve a machine learning model using scikit-learn

Write automated tests with pytest

Create a Continuous Integration pipeline using GitHub Actions

Automatically run tests on every push or pull request

Apply software engineering best practices (modular code, tests, requirements file)

This project imitates a real-world ML microservice pipeline used in industry.
2.Project Structure 
ml-api-ci-cd-demo/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI application with endpoints
│   └── model.py       # ML model (RandomForest trained on Iris dataset)
│
├── tests/
│   ├── __init__.py
│   └── test_api.py    # Pytest test suite for API endpoints
│
├── requirements.txt    # Python dependencies
│
├── .gitignore          # Ignore venv, pycache, etc.
│
└── .github/
    └── workflows/
        └── ci.yml     # GitHub Actions CI pipeline
3. Machine Learning Component

The ML model lives in app/model.py.

📌 Key details:

Model: RandomForestClassifier

Dataset: Iris dataset (included in scikit-learn)

Training happens automatically at startup

Prediction returns the class name (setosa, versicolor, virginica)
.

🚀 4. FastAPI Application

File: app/main.py

Endpoints:
1. /health

Method: GET

Returns:

{"status": "ok"}


Used by monitoring systems to check if the app is alive.

2. /predict

Method: POST

Input JSON:

{
  "features": [5.1, 3.5, 1.4, 0.2]
}


Output JSON:

{
  "predicted_class": "setosa"
}

Validation:

Must contain exactly 4 features

Otherwise returns a 400 error

5. Automated Tests (Pytest)

File: tests/test_api.py

Tests included:

1. Health endpoint test

Ensures the API runs.

2. Valid prediction test

Checks:

API returns 200 status

Response contains "predicted_class"

3. Invalid input test

Ensures the API rejects wrong-length feature arrays.



⚙️ 6. Continuous Integration (GitHub Actions)

File: .github/workflows/ci.yml

Trigger:

Runs on:

any push to main

any pull request targeting main

Pipeline Steps:

Checkout code

Set up Python 3.10

Install dependencies

Run pytest

Why CI is important:

Ensures the code works before deployment

Prevents broken ML models from reaching production

Gives confidence in refactoring

Required in most real-world companies


🔄 7. Requirements File

requirements.txt lists all packages needed:

fastapi
uvicorn[standard]
scikit-learn
pytest
httpx


GitHub Actions uses this file to recreate the environment for testing.

🛡️ 8. Git Hygiene & Best Practices Implemented

✔ .gitignore used to avoid committing venv
✔ Clean commit history
✔ Proper project structure
✔ Automated tests
✔ CI pipeline
✔ Predictable environment via requirements.txt

💬 9. How to Run the Project Locally
1. Create virtual environment
python -m venv venv
source venv/Scripts/activate

2. Install dependencies
pip install -r requirements.txt

3. Run FastAPI server
uvicorn app.main:app --reload

4. Open docs:

http://127.0.0.1:8000/docs

5. Run tests:
pytest

🧩 10. Architecture Diagram
        ┌──────────────┐          
        │ Client        │          
        │ (Postman/UI)  │          
        └───────┬──────┘          
                │                
          HTTP Request           
                │                
        ┌───────▼─────────┐      
        │   FastAPI App   │      
        │   main.py       │      
        └───────┬─────────┘      
                │                
     loads model on startup       
                │                
        ┌───────▼─────────┐      
        │   ML Model      │      
        │  model.py       │      
        └───────┬─────────┘      
                │                
        ┌───────▼──────────┐     
        │  scikit-learn     │     
        └───────────────────┘     

📡 11. CI Pipeline Diagram
    GitHub Repo
        |
        | push / PR
        v
┌────────────────────────────┐
│ GitHub Actions CI Pipeline │
├────────────────────────────┤
│ 1. Checkout code           │
│ 2. Setup Python            │
│ 3. Install Dependencies    │
│ 4. Run pytest              │
│ 5. Report Status           │
└────────────────────────────┘
        |
        v
     PASS / FAIL
