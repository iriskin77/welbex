from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from car.schema import CreateCarRequest
from car import services
from load_data import load


router_car = APIRouter()


@router_car.post("/")
async def create_car(car: CreateCarRequest):
    try:
        new_car = await services.create_car(car=car)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return new_car


@router_car.patch("/")
async def update_car():
    try:
        await services.update_all_cars_location()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return JSONResponse({"cars locations updated successfully": 201})


@router_car.post("/upload_cars")
async def upload_cars():
    try:
        await load.load_cards()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return JSONResponse({"cars uploaded successfully": 201})
