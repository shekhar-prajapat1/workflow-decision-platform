
def check_credit_api(score):

    # simulate external dependency failure
    if score < 300:
        raise Exception("External credit service unavailable")

    return True
