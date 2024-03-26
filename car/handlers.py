from fastapi import APIRouter, Depends, HTTPException
from car.schema import CreateCarRequest
from car import services


router_car = APIRouter()


@router_car.post("/")
async def create_car(car: CreateCarRequest):
    car = await services.create_car(car=car)
    return car


@router_car.patch("/")
async def update_car():
    pass
