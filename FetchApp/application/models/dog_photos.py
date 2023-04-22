from datetime import date
from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


@dataclass
class DogPhoto(db.Model):
    __tablename__ = 'dog_photos'

    id: int
    dog_id: int
    photo: str

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    dog_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('dog.id'))
    photo: Mapped[str] = mapped_column(db.String)

    dog: Mapped[List["Dog"]] = relationship("Dog", back_populates='dog_photo')
