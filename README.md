# Configurable Workflow Decision Platform

## Overview

This project implements a **configurable workflow-based decision platform** that evaluates requests using rule-based workflows.

The platform supports **multiple business workflows** and allows business rules to be modified through configuration without changing the core application code.

Example workflows supported:

- Loan Approval (Finance)
- Vendor Approval (Procurement)
- Employee Onboarding (HR)

The system uses a **rule engine and workflow engine architecture** to process requests and return decisions such as **approve, reject, or manual review**.

---

# Key Features

- Configurable workflow rules
- Multiple business workflows
- Rule-based decision engine
- REST API using FastAPI
- Minimal UI for interaction
- External dependency simulation
- Audit logging for traceability
- Input validation for workflows
- Modular architecture

---

# System Architecture
Frontend UI (HTML)
│
▼
FastAPI REST API
│
▼
Workflow Engine
│
▼
Rule Engine
│
▼
Workflow Configuration
│
▼
Decision + Audit Logs


---

# Components

| Component | Description |
|--------|--------|
Frontend UI | Minimal web interface to submit workflow requests |
FastAPI API | Handles incoming requests |
Workflow Engine | Coordinates workflow execution |
Rule Engine | Evaluates configurable rules |
Workflow Config | Stores workflow rules |
Audit Logger | Logs decision history |
External Service | Simulated credit check service |

---

# Project Structure
decision-platform/

main.py

engine/
workflow_engine.py
rule_engine.py

config/
workflow_config.py

services/
credit_service.py

audit/
logger.py

database/
db.py

static/
index.html

tests/
test_workflows.py

README.md


---

# Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- Pytest
- Requests

Install dependencies:

---

# Installation

### Clone the repository
git clone <repository-url>
cd decision-platform


---

# Running the Application

Start the server:


python -m uvicorn main:app --reload


Server will start at:


http://127.0.0.1:8000


Open the link in your browser to access the UI.

---

# API Interface

### Endpoint


POST /process


---

# Example Requests

## Loan Approval


{
"workflow": "loan_approval",
"amount": 5000,
"credit_score": 720
}


Possible outcomes:

- approve
- reject
- manual_review

---

## Vendor Approval


{
"workflow": "vendor_approval",
"vendor_rating": 4,
"contract_value": 200000,
"years_in_business": 5,
"vendor_blacklisted": false
}


---

## Employee Onboarding


{
"workflow": "employee_onboarding",
"background_check": true,
"experience_years": 3,
"education_level": 4,
"previous_company_verified": true
}


---

# Example API Response


{
"request_id": "b6d1a9e3-3f7a-4e2a-a1d4-1c8c5e0a6d1a",
"workflow": "loan_approval",
"status": "approve",
"reason": "Loan approved"
}


---

# Example Decision Explanation

Input:


amount = 5000
credit_score = 720


Rules evaluated:


credit_score < 600 → False
amount > 100000 → False
default → True


Decision:


approve


---

# Configuration Model

Workflow rules are defined in:


config/workflow_config.py


Example rule:


{
"rule": "credit_score < 600",
"action": "reject",
"reason": "Low credit score"
}


New workflows can be added **without changing application code**.

---

# External Dependency Simulation

The platform simulates an external credit service.

File:


services/credit_service.py


Example failure:


External credit service unavailable


This demonstrates system resilience when external dependencies fail.

---

# Audit Logging

Every decision is logged.

File:


audit/logger.py


Example log:


AUDIT LOG
timestamp: 2026-03-14
request: {...}
decision: approve
reason: Loan approved


This ensures **traceability and explainability of decisions**.

---

# Idempotency

Each request is assigned a unique identifier:


request_id = uuid.uuid4()


This helps track and identify duplicate or retried requests.

---

# Running Tests

Start the API server:


python -m uvicorn main:app --reload


Then run automated tests:


python -m pytest


Test coverage includes:

- Happy path workflow execution
- Invalid input validation
- Dependency failure simulation
- Vendor approval workflow
- Employee onboarding workflow

---

# Scaling Considerations

For production systems the platform could scale using:

- Multiple FastAPI instances behind a load balancer
- Redis for idempotency storage
- Kafka or message queues for asynchronous workflow processing
- Distributed rule caching
- Containerized deployment using Docker and Kubernetes

---

# Design Tradeoffs

| Design Choice | Reason |
|--------|--------|
Rule-based engine | Allows flexible business logic |
Config-driven workflows | Enables rule updates without code changes |
FastAPI | Lightweight and high-performance API framework |

---

# Future Improvements

Possible future enhancements include:

- Database-based idempotency tracking
- Graphical workflow editor for rule configuration
- Asynchronous workflow processing
- Monitoring and metrics collection
- Authentication and authorization support

---

# Test Scenarios

The system supports testing for:

- Happy path workflow execution
- Invalid input validation
- External dependency failure
- Rule change scenarios
- Multiple workflow types

---

# Conclusion

This project demonstrates how a **configurable workflow decision platform** can support multiple business units using a flexible rule engine architecture while maintaining traceability, scalability, and reliability.