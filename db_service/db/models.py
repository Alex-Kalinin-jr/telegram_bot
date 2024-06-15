from typing import Optional, List
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import Mapped


# ALL THE MODULE TO BE REFACTORED. AT THE SAME TYPE bot_service/test_router, bot_service/utils, router - TO BE REFACTORED, 

class Categories(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str = Field(...)
    description: Optional[str] = Field(default="описание отсутствует")

    position: Mapped[List["Positions"]] = Relationship(back_populates="category")


class Positions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    position: str = Field(...)
    category_id: Optional[int] = Field(default=None, foreign_key="categories.id")
    description: Optional[str] = Field(default="описание отсутствует")

    links: Mapped[List["Links"]] = Relationship(back_populates="position")
    category: Mapped[Categories] = Relationship(back_populates="position")


class Links(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    position_id: Optional[int] = Field(default=None, foreign_key="positions.id", index=True)
    img: Optional[str] = Field(default=None)

    position: Mapped[Positions] = Relationship(back_populates="links")

