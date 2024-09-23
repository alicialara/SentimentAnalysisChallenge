from transformers import pipeline

# Load the sentiment analysis model
sentiment_analysis = pipeline(
    "sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment"
)


def analyze_text(text: str):
    """
    Analyze the sentiment of the given text using the preloaded model.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: The result containing the label and score.
    """
    result = sentiment_analysis(text)[0]
    return result
