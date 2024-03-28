from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from . import services
from .schema import LocationListResponse


router_location = APIRouter()


@router_location.get("/upload_uszips")
async def load_uszips():
    """"Добавляет локации из файла uszips.csv"""""
    try:
        await services.load_uszips()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return JSONResponse({"status": 201})


@router_location.get("/", response_model=LocationListResponse)
async def get_uszips(limit: int):
    """"Получение списка локаций"""""
    try:
        locations = await services.get_uszips(limit=limit)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return {"locations": locations}

