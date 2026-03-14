
import datetime
from database.db import insert_audit

def log_decision(request, decision):

    log = {
        "timestamp": str(datetime.datetime.now()),
        "request": request,
        "decision": decision
    }

    insert_audit(log)

    print("AUDIT LOG:", log)
