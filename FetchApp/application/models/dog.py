from datetime import date
from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


@dataclass
class Dog(db.Model):
    __tablename__ = 'dog'

    id: int
    user_id: str
    dog_name: str
    dog_age: str
    type_id: int
    description: str

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(db.String, db.ForeignKey('user.id'))
    dog_name: Mapped[str] = mapped_column(db.String)
    dog_age: Mapped[str] = mapped_column(db.String)
    type_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('dog_type.id'))
    description: Mapped[str] = mapped_column(db.String)

    user: Mapped[List["User"]] = relationship("User", back_populates='dog')
    dog_type: Mapped[List["DogType"]] = relationship("DogType", back_populates='dog')
    dog_photo: Mapped[List["DogPhoto"]] = relationship("DogPhoto", back_populates='dog')
