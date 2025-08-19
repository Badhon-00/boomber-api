from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from twilio.rest import Client
import os

router = APIRouter()

try:
    client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_TOKEN'))
except Exception as e:
    raise RuntimeError(f"Twilio init failed: {str(e)}")

class SMSRequest(BaseModel):
    to: str
    message: str

@router.post("/send")
async def send_sms(request: SMSRequest):
    try:
        msg = client.messages.create(
            body=request.message,
            from_=os.getenv('TWILIO_PHONE'),
            to=request.to
        )
        return {
            "status": "success",
            "sid": msg.sid,
            "to": request.to
        }
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"SMS failed: {str(e)}"
        )