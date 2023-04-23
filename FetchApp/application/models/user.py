from datetime import date
from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


@dataclass
class User(db.Model):
    __tablename__ = 'user'

    id: int
    first_name: str
    last_name: str
    city: str
    phone: str
    email: str
    password: str
    user_type: str
    bio: str

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String)
    last_name: Mapped[str] = mapped_column(db.String)
    city: Mapped[str] = mapped_column(db.String)
    phone: Mapped[str] = mapped_column(db.String)
    email: Mapped[str] = mapped_column(db.String)
    password: Mapped[str] = mapped_column(db.String)
    user_type: Mapped[str] = mapped_column(db.String)
    bio: Mapped[str] = mapped_column(db.String)

    dog: Mapped[List["Dog"]] = relationship("Dog", back_populates='user', cascade="all, delete-orphan")
    sitter_type_link: Mapped[List["SitterTypeLink"]] = relationship("SitterTypeLink", back_populates='user')
