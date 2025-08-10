from pydantic import BaseModel
from typing import Literal


class MessageRequest(BaseModel):
    msg: str
    role: Literal["admin", "student", "mentor"]

class MessageResponse(BaseModel):
    status: str
    message: str

    class Config:
        json_schema_extra = {
            "example": {
                "status": "ok",
                "message": "Сообщение получено"
            }
        }
