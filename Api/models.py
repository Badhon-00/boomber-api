from pydantic import BaseModel

class SMSRequest(BaseModel):
    to: str
    message: str