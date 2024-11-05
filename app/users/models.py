import enum
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from typing import Literal
from typing import get_args
from sqlalchemy import Enum
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM as PgEnum

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship



class Roles(Enum):
    admin: str = "admin"
    user: str = "user"


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False)
    roles = Column(PgEnum(Roles, name="roles", create_type=True), nullable=False, default=Roles.user)
    messages_sent = relationship("Message", foreign_keys="[Message.sender_id]", cascade="all, delete-orphan")
    messages_received = relationship("Message", foreign_keys="[Message.recipient_id]", cascade="all, delete-orphan")
