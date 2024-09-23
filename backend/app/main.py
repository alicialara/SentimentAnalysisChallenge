from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from .services import analyze_text


app = FastAPI()

# Allow CORS for all origins (you can restrict this to specific origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class TextRequest(BaseModel):
    text: str


@app.post("/analyze")
async def analyze_sentiment(request: TextRequest):
    """
    Analyze the sentiment of the provided text.

    Args:
        request (TextRequest): The request object containing the text to be analyzed.

    Returns:
        dict: A dictionary containing the sentiment analysis results.
    """
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    # Analyze the text
    result = analyze_text(text)

    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
