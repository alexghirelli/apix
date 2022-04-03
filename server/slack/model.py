from pydantic import BaseModel

class StatusSchema(BaseModel):
    status_text: str
    status_emoji: str
    status_expiration: str
