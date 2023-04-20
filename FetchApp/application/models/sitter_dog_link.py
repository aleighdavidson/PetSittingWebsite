from datetime import date
from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


@dataclass
class SitterDogLink(db.Model):
    __tablename__ = 'sitter_dog_link'

    link_id: int
    dog_type_id: int
    sitter_type_id: int

    link_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    dog_type_id: Mapped[int] = mapped_column(db.Integer)
    sitter_type_id: Mapped[int] = mapped_column(db.Integer)

    # dog_type: Mapped[List["DogType"]] = relationship("DogType", back_populates='sitter_dog_link')
    # sitter_type: Mapped[List["SitterType"]] = relationship("SitterType", back_populates='sitter_dog_link')
