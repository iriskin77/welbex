from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from location.models import Location

router_location = APIRouter()

uszips = pd.read_csv("/home/abc/Рабочий стол/welbex/uszips/uszips.csv")


@router_location.get("/load_uszips")
async def load_uszips():
    uszips_to_add = uszips[["zip", "latitude", "longitude", "city", "state"]]
    await Location.bulk_create([Location(**item) for item in uszips_to_add.to_dict('records')])
    return JSONResponse({"status": 201})


@router_location.get("/load_cars")
async def load_cars():
    pass

