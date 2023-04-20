from datetime import date
from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


@dataclass
class SitterTypeLink(db.Model):
    __tablename__ = 'sitter_type_link'

    link_id: int
    user_id: int
    sitter_type_id: int

    link_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('user.id'))
    sitter_type_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('sitter_type.sitter_type_id'))

    #user: Mapped[List["User"]] = relationship("User", back_populates='sitter_type_link')
    sitter_type: Mapped[List["SitterType"]] = relationship("SitterType", back_populates='sitter_type_link')
