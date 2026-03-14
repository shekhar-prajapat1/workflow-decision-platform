class RuleEngine:

    def evaluate(self, request, rules):

        for rule in rules:

            # handle default rule
            if rule["rule"] == "default":
                return rule

            try:
                result = eval(rule["rule"], {}, request)

                if result:
                    return rule

            except Exception:
                # Skip rule if variable not in request
                continue

        return None