from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from location.models import Location
from load_data import load

router_location = APIRouter()

uszips = pd.read_csv("/home/abc/Рабочий стол/welbex/load_data/uszips.csv")


@router_location.get("/load_uszips")
async def load_uszips():
    await load.load_uszips(uszips)
    return JSONResponse({"status": 201})

