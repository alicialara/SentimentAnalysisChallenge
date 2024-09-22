from transformers import pipeline

from backend.app.utils import get_db_connection

# Load the sentiment analysis model
sentiment_analysis = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

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

def create_sentiment_table():
    """
    Create the sentiment_results table in the database if it does not exist.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sentiment_results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            text TEXT NOT NULL,
            label VARCHAR(50) NOT NULL,
            score FLOAT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()