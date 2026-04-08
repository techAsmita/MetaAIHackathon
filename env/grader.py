def grade(response):
    response = response.lower()

    score = 0.0

    if "sorry" in response:
        score += 0.3

    if "refund" in response:
        score += 0.4

    if len(response) > 20:
        score += 0.3

    # CRITICAL FIX
    if score >= 1.0:
        score = 0.95
    elif score <= 0.0:
        score = 0.05

    return score
