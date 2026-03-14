from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from engine.workflow_engine import WorkflowEngine
from config.workflow_config import WORKFLOW_RULES
from audit.logger import log_decision
from database.db import init_db

import uuid

app = FastAPI()

engine = WorkflowEngine()

# Initialize database
init_db()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Home page
@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html") as f:
        return f.read()


# Main workflow processing endpoint
@app.post("/process")
def process(data: dict):

    try:

        workflow = data.get("workflow")

        if not workflow:
            raise HTTPException(status_code=400, detail="Workflow is required")

        if workflow not in WORKFLOW_RULES:
            raise HTTPException(status_code=400, detail="Invalid workflow type")

        # -------------------------------
        # WORKFLOW VALIDATION
        # -------------------------------

        if workflow == "loan_approval":

            required_fields = [
                "amount",
                "credit_score"
            ]

        elif workflow == "vendor_approval":

            required_fields = [
                "vendor_rating",
                "contract_value",
                "years_in_business",
                "vendor_blacklisted"
            ]

        elif workflow == "employee_onboarding":

            required_fields = [
                "background_check",
                "experience_years",
                "education_level",
                "previous_company_verified"
            ]

        else:
            required_fields = []

        # Validate required fields
        for field in required_fields:
            if field not in data:
                raise HTTPException(
                    status_code=400,
                    detail=f"{workflow} requires {field}"
                )

        # -------------------------------
        # CREATE REQUEST ID
        # -------------------------------

        request_id = str(uuid.uuid4())
        data["request_id"] = request_id

        # -------------------------------
        # LOAD WORKFLOW RULES
        # -------------------------------

        rules = WORKFLOW_RULES[workflow]

        # -------------------------------
        # PROCESS DECISION ENGINE
        # -------------------------------

        result = engine.process(data, rules)

        # -------------------------------
        # AUDIT LOGGING
        # -------------------------------

        log_decision(data, result)

        # -------------------------------
        # RESPONSE
        # -------------------------------

        return {
            "request_id": request_id,
            "workflow": workflow,
            "status": result["status"],
            "reason": result["reason"]
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))