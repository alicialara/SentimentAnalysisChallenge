from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)

def test_analyze_sentiment():
    response = client.post("/analyze", json={"text": "Me encanta hacer retos de NLP!"})
    assert response.status_code == 200
    result = response.json()
    assert "label" in result
    assert "score" in result
    assert "timestamp" in result
    assert result["label"] in ["POSITIVE", "NEGATIVE"]

def test_analyze_sentiment_no_text():
    response = client.post("/analyze", json={"text": ""})
    assert response.status_code == 400
    result = response.json()
    assert result["detail"] == "Sin texto proporcionado"