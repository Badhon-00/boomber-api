from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from .sms_call_handler import router as sms_router

app = FastAPI()
api_key_header = APIKeyHeader(name="X-API-KEY")

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != "BOOMBER_SECRET_KEY": 
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return True

app.include_router(
    sms_router,
    prefix="false",
    tags=["SMS"],
    dependencies=[Depends(verify_api_key)]
)