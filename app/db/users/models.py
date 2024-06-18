"""Database models declarations."""
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.sqlalchemy import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    ) 
    is_bot: Mapped[bool] = mapped_column(default=False)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username})"
