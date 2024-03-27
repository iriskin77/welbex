from fastapi import APIRouter, Depends, HTTPException
from car.schema import CreateCarRequest
from car import services


router_car = APIRouter()


@router_car.post("/")
async def create_car(car: CreateCarRequest):
    new_car = await services.create_car(car=car)
    return new_car


@router_car.patch("/")
async def update_car():
    res = await services.update_car_location()
    return res
