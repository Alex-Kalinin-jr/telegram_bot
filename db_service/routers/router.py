import json

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from db.database import get_session, AsyncSession
from db.models import *


router = APIRouter()

@router.get("/getall", status_code=200)
async def response_hello():
    return {"hello" : "world"}


@router.get("/categories", status_code=200, response_model=List[Categories])
async def get_categories(*, session: AsyncSession=Depends(get_session)):
    categories = await session.exec(select(Categories).distinct())

    if not categories:
        raise HTTPException(status_code=404, detail="Answers not found")

    return categories.all()


@router.get("{category}", status_code=200)
async def get_positions_by_category(*, session: AsyncSession=Depends(get_session), category: str):
    positions = await session.exec(select(Categories.position).where(Categories.name == category))
    pos_dict = [{pos["name"], pos["description"]} for pos in positions]
    return pos_dict
