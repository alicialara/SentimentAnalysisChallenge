from pydantic import BaseModel


class SentimentResult(BaseModel):
    """
    Represents the result of a sentiment analysis.

    Attributes:
        text (str): The original text that was analyzed.
        label (str): The sentiment label (e.g., positive, negative, neutral).
        score (float): The confidence score of the sentiment analysis.
    """

    text: str
    label: str
    score: float
