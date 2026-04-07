def grade(response):
    response = response.lower()

    score = 0
    if "sorry" in response:
        score += 0.3
    if "refund" in response:
        score += 0.4
    if len(response) > 20:
        score += 0.3

    return score