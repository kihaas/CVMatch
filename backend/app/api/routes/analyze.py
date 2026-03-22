from fastapi import APIRouter
from ...schemas.analyze import AnalyzeRequest, AnalyzeResponse

router = APIRouter(tags=["analyze"])

@router.post("/api/analyze", response_model=AnalyzeResponse)
async def analyze(request: AnalyzeRequest):
    return AnalyzeResponse(
        match_score=75.0,
        present_skills=["Python", "FastAPI"],
        missing_skills=["Docker", "Redis"],
        summary="Кандидат подходит частично",
        improved_bullets=["Разработала REST API на FastAPI"]
    )