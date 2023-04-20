from datetime import date
from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


@dataclass
class SitterType(db.Model):
    __tablename__ = 'sitter_type'

    sitter_type_id: int
    sitter_type: str

    sitter_type_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    sitter_type: Mapped[str] = mapped_column(db.String)

    sitter_type_link: Mapped[List["SitterTypeLink"]] = relationship("SitterTypeLink", back_populates='sitter_type')
    # sitter_dog_link: Mapped[List["SitterDogLink"]] = relationship("SitterDogLink", back_populates='sitter_type')
