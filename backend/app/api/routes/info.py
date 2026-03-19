


router = APIRouter(prefix="/api", tags=["info"])

@router.get("/about")
async def about():
    return {"text": "..."}

@router.get("/contacts")
async def contacts():
    return {"email": "...", "telegram": "..."}
