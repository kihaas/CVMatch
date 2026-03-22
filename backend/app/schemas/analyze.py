from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    vacancy_text: str
    resume_text: str

class AnalyzeResponse(BaseModel):
    match_score: float
    present_skills: list[str]
    missing_skills: list[str]
    summary: str
    improved_bullets: list[str]