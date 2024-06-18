
import datetime
from pydantic import BaseModel, ConfigDict


class MessageDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date: datetime.datetime
    text: str | None = None
    file_id: str | None = None
    mime_type: str | None = None
    file_size: int | None = None
    chat_id: str
    user_id: int
