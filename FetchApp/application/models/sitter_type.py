from datetime import date
from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


@dataclass
class SitterType(db.Model):
    __tablename__ = 'sitter_type'

    sitter_type_id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    sitter_type: Mapped[str] = mapped_column(db.String)
