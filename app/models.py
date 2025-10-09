from app import db,login
from typing import Optional
from datetime import datetime,timezone
from werkzeug.security import generate_password_hash,check_password_hash
import sqlalchemy as sa
from sqlalchemy.orm import Mapped,mapped_column
from flask_login import UserMixin


class User(db.Model,UserMixin):
    id:Mapped[int] = mapped_column(sa.Integer,primary_key=True)
    username:Mapped[str] = mapped_column(sa.String(64),index=True)
    email:Mapped[str] = mapped_column(sa.String(64),index=True, unique=True)
    password_hash:Mapped[Optional[str]] = mapped_column(sa.String(256))
    created_at:Mapped[datetime] = mapped_column(sa.DateTime, 
                                                default=lambda: datetime.now(timezone.utc))
    
    # setting up password hash
    def set_password_hash(self,password):
        self.password_hash = generate_password_hash(password)
    
    # checking user password
    def check_password_hash(self,password):
        return check_password_hash(self.password_hash,password)

    # setting up the user loader function
    @login.user_loader
    def user_loader(id):
        return db.session.get(User,int(id))

    def __repr__(self):
        return f"<User {self.username}>"