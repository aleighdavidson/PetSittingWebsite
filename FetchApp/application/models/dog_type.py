from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


@dataclass
class DogType(db.Model):
    __tablename__ = 'dog_type'

    id: int
    type: str
    description: str

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    type: Mapped[str] = mapped_column(db.String)
    description: Mapped[str] = mapped_column(db.String)

    dog: Mapped[List["Dog"]] = relationship("Dog", back_populates='dog_type')
