from datetime import date
from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


@dataclass
class DogPhoto(db.Model):
    __tablename__ = 'dog_photos'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    dog_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('dog.id'))
    photo: Mapped[str] = mapped_column(db.String)