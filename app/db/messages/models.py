"""Database models declarations."""
import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.sqlalchemy import Base


class MessageModel(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(
        primary_key=True
    ) 
    date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    text: Mapped[str] = mapped_column(nullable=True)
    file_id: Mapped[str] = mapped_column(nullable=True)
    mime_type: Mapped[str] = mapped_column(nullable=True)
    file_size: Mapped[int] = mapped_column(nullable=True)
    chat_id: Mapped[str] = mapped_column(ForeignKey("chats.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


    def __repr__(self) -> str:
        return f"Message(id={self.id}, date={self.date})"
