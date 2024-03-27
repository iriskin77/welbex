from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from car.schema import CreateCarRequest
from car import services
from load_data import load


router_car = APIRouter()


@router_car.post("/")
async def create_car(car: CreateCarRequest):
    new_car = await services.create_car(car=car)
    return new_car


@router_car.patch("/")
async def update_car():
    await services.update_all_cars_location()
    return JSONResponse({"cars locations updated successfully": 201})


@router_car.post("/upload_cars")
async def upload_cars():
    await load.load_cards()
    return JSONResponse({"cars uploaded successfully": 201})
