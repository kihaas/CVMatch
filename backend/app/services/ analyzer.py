async def analyze_resume(vacancy_text: str, resume_text: str) -> AnalyzeResponse:
    raw = await ai_client.analyze(vacancy_text, resume_text)
    return AnalyzeResponse(**raw)
