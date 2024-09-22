from fastapi import APIRouter

from backend.app.main import TextRequest, analyze_sentiment

router = APIRouter()

@router.post("/analyze")
async def analyze_sentiment_route(request: TextRequest):
    return await analyze_sentiment(request)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app.main:app", host='0.0.0.0', port=5000, reload=True)