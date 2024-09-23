from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_analyze_sentiment():
    response = client.post("/analyze", json={"text": "Me encanta hacer retos de NLP!"})
    assert response.status_code == 200
    result = response.json()
    assert "label" in result
    assert "score" in result
    assert result["label"] in ["1 star", "2 stars", "3 stars", "4 stars", "5 stars"]


def test_analyze_sentiment_no_text():
    response = client.post("/analyze", json={"text": ""})
    assert response.status_code == 400
    result = response.json()
    assert result["detail"] == "No text provided"
