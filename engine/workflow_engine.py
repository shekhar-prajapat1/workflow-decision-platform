from engine.rule_engine import RuleEngine
from services.credit_service import check_credit_api

class WorkflowEngine:

    def __init__(self):
        self.rule_engine = RuleEngine()

    def process(self, request, rules):

        # Only call credit service if credit_score exists
        if "credit_score" in request:
            try:
                check_credit_api(request["credit_score"])
            except Exception as e:
                raise Exception(str(e))

        decision = self.rule_engine.evaluate(request, rules)

        if not decision:
            raise Exception("No matching rule found")

        result = {
            "status": decision["action"],
            "reason": decision["reason"]
        }

        return result