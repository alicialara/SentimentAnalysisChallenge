from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from .services import analyze_text

# from .utils import get_db_connection

app = FastAPI()

# Allow CORS for all origins (you can restrict this to specific origins if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# @app.on_event("startup")
# async def startup_event():
#     create_sentiment_table()


class TextRequest(BaseModel):
    text: str


@app.post("/analyze")
async def analyze_sentiment(request: TextRequest):
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    # Analyze the text
    result = analyze_text(text)

    # # Store the result in the database
    # conn = get_db_connection()
    # cur = conn.cursor()
    # cur.execute("INSERT INTO sentiment_results (text, label, score) VALUES (%s, %s, %s)",
    #             (text, result['label'], result['score']))
    # conn.commit()
    # cur.close()
    # conn.close()

    return result


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
