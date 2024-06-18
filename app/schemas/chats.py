from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict



class ChatDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    type: str
    title: str
    deleted: bool
