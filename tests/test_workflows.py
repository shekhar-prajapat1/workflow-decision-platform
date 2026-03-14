import requests

BASE_URL = "http://127.0.0.1:8000/process"


# ------------------------
# HAPPY PATH TEST
# ------------------------

def test_loan_approval():

    payload = {
        "workflow": "loan_approval",
        "amount": 5000,
        "credit_score": 720
    }

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["status"] in ["approve", "manual_review"]



# ------------------------
# INVALID INPUT TEST
# ------------------------

def test_invalid_input():

    payload = {
        "workflow": "loan_approval",
        "amount": 5000
    }

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 400



# ------------------------
# VENDOR WORKFLOW TEST
# ------------------------

def test_vendor_approval():

    payload = {
        "workflow": "vendor_approval",
        "vendor_rating": 4,
        "contract_value": 200000,
        "years_in_business": 5,
        "vendor_blacklisted": False
    }

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["status"] in ["approve", "manual_review"]



# ------------------------
# EMPLOYEE WORKFLOW TEST
# ------------------------

def test_employee_onboarding():

    payload = {
        "workflow": "employee_onboarding",
        "background_check": True,
        "experience_years": 3,
        "education_level": 4,
        "previous_company_verified": True
    }

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 200



# ------------------------
# DEPENDENCY FAILURE TEST
# ------------------------

def test_credit_service_failure():

    payload = {
        "workflow": "loan_approval",
        "amount": 5000,
        "credit_score": 200
    }

    response = requests.post(BASE_URL, json=payload)

    assert response.status_code == 503