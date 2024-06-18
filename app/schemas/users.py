from pydantic import BaseModel, ConfigDict



class UserDB(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_bot: bool = False
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
