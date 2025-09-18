from app import db
from typing import Optional
from datetime import datetime,timezone
import sqlalchemy as sa
from sqlalchemy.orm import Mapped,mapped_column


class User(db.Model):
    id:Mapped[int] = mapped_column(sa.Integer,primary_key=True)
    username:Mapped[str] = mapped_column(sa.String(64),index=True)
    email:Mapped[str] = mapped_column(sa.String(64),index=True, unique=True)
    password_hash:Mapped[Optional[str]] = mapped_column(sa.String(256))
    created_at:Mapped[datetime] = mapped_column(sa.DateTime, 
                                                default=lambda: datetime.now(timezone.utc))

    def __repr__(self):
        return f"<User {self.username}>"