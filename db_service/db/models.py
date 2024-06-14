from typing import Optional, List
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Enum as SqlEnum


class Categories(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str = Field(...)
    description: Optional[str] = Field(default="описание отсутствует")

    position: "Positions" = Relationship(back_populates="category")  # Forward reference still needed


class Positions(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    position: str = Field(...)
    category_id: Optional[int] = Field(default=None, foreign_key="categories.id")  # Reference table name in string
    description: Optional[str] = Field(default="описание отсутствует")

    links: List["Links"] = Relationship(back_populates="position")
    category: Categories = Relationship(back_populates="position")


class Links(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    position_id: Optional[int] = Field(default=None, foreign_key="positions.id", index=True)
    img: Optional[str] = Field(default=None)

    position: Positions = Relationship(back_populates="links")