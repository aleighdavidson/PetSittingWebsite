from datetime import date
from application import db
from dataclasses import dataclasses
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Sitter_type_link(db.Model):

    @dataclass
    __tablename__ = 'sitter_type_link'

    link_id: int
    user_id: int
    sitter_type_id: int

    link_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(db.Integer)
    sitter_type_id: Mapped[int] = mapped_column(db.Integer)
