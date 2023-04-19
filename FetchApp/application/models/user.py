from datetime import date
from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


@dataclass
class User(db.Model):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String)
    last_name: Mapped[str] = mapped_column(db.String)
    city: Mapped[str] = mapped_column(db.String)
    phone: Mapped[str] = mapped_column(db.String)
    email: Mapped[str] = mapped_column(db.String)
    password: Mapped[str] = mapped_column(db.String)
    user_type: Mapped[str] = mapped_column(db.String)
    bio: Mapped[str] = mapped_column(db.String)
