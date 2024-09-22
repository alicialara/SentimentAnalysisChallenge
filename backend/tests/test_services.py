from backend.app.services import analyze_text


def test_analyze_text_positive():
    result = analyze_text("Me encanta esta aplicación, qué interesante!")
    assert "label" in result
    assert "score" in result
    assert result["label"] == "POSITIVE"


def test_analyze_text_negative():
    result = analyze_text("Odio esta aplicación, qué aburrida!")
    assert "label" in result
    assert "score" in result
    assert result["label"] == "NEGATIVE"
