"""Database models declarations."""
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.sqlalchemy import Base


class ChatModel(Base):
    __tablename__ = "chats"

    id: Mapped[str] = mapped_column(
        primary_key=True
    ) 
    type: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column()
    deleted: Mapped[bool] = mapped_column(default=False)

    def __repr__(self) -> str:
        return f"Chat(id={self.id}, type={self.type}, title={self.title})"
