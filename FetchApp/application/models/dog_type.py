from application import db
from dataclasses import dataclass
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

@dataclass
class DogType(db.Model):
    __tablename__ = 'dog_type'

    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    type: Mapped[str] = mapped_column(db.String)
    description: Mapped[str] = mapped_column(db.String)
