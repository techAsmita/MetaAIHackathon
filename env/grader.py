def grade(response):
    response = response.lower()

    score = 0.0

    if "sorry" in response:
        score += 0.3

    if "refund" in response:
        score += 0.4

    if len(response) > 20:
        score += 0.3

    # FINAL SAFE CLAMP
    score = max(0.01, min(score, 0.99))

    return float(score)
