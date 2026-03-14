WORKFLOW_RULES = {

    # -----------------------------
    # LOAN APPROVAL WORKFLOW
    # -----------------------------
    "loan_approval": [

        {
            "rule": "credit_score < 600",
            "action": "reject",
            "reason": "Low credit score"
        },

        {
            "rule": "amount > 100000",
            "action": "manual_review",
            "reason": "High loan amount requires review"
        },

        {
            "rule": "default",
            "action": "approve",
            "reason": "Loan approved"
        }

    ],


    # -----------------------------
    # VENDOR APPROVAL WORKFLOW
    # -----------------------------
    "vendor_approval": [

        {
            "rule": "vendor_blacklisted == True",
            "action": "reject",
            "reason": "Vendor is blacklisted"
        },

        {
            "rule": "vendor_rating < 3",
            "action": "reject",
            "reason": "Vendor rating too low"
        },

        {
            "rule": "years_in_business < 2",
            "action": "manual_review",
            "reason": "Vendor business history too short"
        },

        {
            "rule": "contract_value > 500000",
            "action": "manual_review",
            "reason": "High contract value requires review"
        },

        {
            "rule": "default",
            "action": "approve",
            "reason": "Vendor approved"
        }

    ],


    # -----------------------------
    # EMPLOYEE ONBOARDING WORKFLOW
    # -----------------------------
    "employee_onboarding": [

        {
            "rule": "background_check == False",
            "action": "reject",
            "reason": "Background check failed"
        },

        {
            "rule": "experience_years < 1",
            "action": "reject",
            "reason": "Insufficient experience"
        },

        {
            "rule": "education_level < 2",
            "action": "manual_review",
            "reason": "Education level requires HR review"
        },

        {
            "rule": "previous_company_verified == False",
            "action": "manual_review",
            "reason": "Previous company verification pending"
        },

        {
            "rule": "default",
            "action": "approve",
            "reason": "Employee onboarding approved"
        }

    ]

}