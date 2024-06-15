import json

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select
from sqlalchemy.orm import joinedload

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


@router.get("/category/{category}", status_code=200, response_model=Categories)
async def get_description_by_category(*, session: AsyncSession=Depends(get_session), category: str):
    category = await session.exec(select(Categories).where(Categories.name == category).distinct())

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category.one()


@router.get("/category_data/{category}", status_code=200)
# @router.get("/category_data/{category}", status_code=200, response_model=list[Positions])
async def get_data_by_category(*, session: AsyncSession=Depends(get_session), category: str):
    positions = await session.exec(select(Categories).where(Categories.name == category).options(joinedload(Categories.position)))
    results = positions.all()
    for result in results:
        print(f"\n{result.position}\n")
    # if not positions:
    #     raise HTTPException(status_code=404, detail="Category not found")

    # return positions.all()
