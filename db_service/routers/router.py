from fastapi import APIRouter

router = APIRouter()

@router.get("/getall", status_code=200)
async def response_hello():
    return {"hello" : "world"}