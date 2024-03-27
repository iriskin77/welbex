from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from .models import Location
from load_data import load
import pandas as pd

router_location = APIRouter()


@router_location.get("/load_uszips")
async def load_uszips():
    try:
        await load.load_uszips()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return JSONResponse({"status": 201})

