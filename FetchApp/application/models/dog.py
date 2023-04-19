from datetime import date
from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import List
from sqlalchemy.orm import relationship

@dataclass
class Dog(db.Model):
    __tablename__ = 'dog'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(db.String, db.ForeignKey('user.id'))
    dog_name: Mapped[str] = mapped_column(db.String)
    type_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('dog_type.id'))
    description: Mapped[str] = mapped_column(db.String)

    user: Mapped[List["User"]] = relationship("User", back_populates='dog')
