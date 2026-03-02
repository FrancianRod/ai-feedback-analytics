import random

def analyze_comment(comment: str) -> dict:
    """
    Mock LLM analysis for portfolio demonstration.
    Simulates classification, sentiment and summary.
    """

    categories = ["Support", "Infrastructure", "System", "Management", "Other"]
    sentiments = ["Positive", "Neutral", "Negative"]

    # Simulação simples baseada em palavras-chave
    comment_lower = comment.lower()

    if "slow" in comment_lower or "wait" in comment_lower:
        sentiment = "Negative"
        score = -0.8
        category = "Support"
        theme = "Service delay"
    elif "clean" in comment_lower or "organized" in comment_lower:
        sentiment = "Positive"
        score = 0.9
        category = "Infrastructure"
        theme = "Facility quality"
    else:
        sentiment = random.choice(sentiments)
        category = random.choice(categories)
        score = round(random.uniform(-1, 1), 2)
        theme = "General feedback"

    summary = f"The feedback is classified as {sentiment} related to {theme}."

    return {
        "category": category,
        "sentiment": sentiment,
        "main_theme": theme,
        "sentiment_score": score,
        "summary": summary
    }