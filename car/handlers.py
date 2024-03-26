from fastapi import APIRouter, Depends, HTTPException
from car import services


router_car = APIRouter()


@router_car.post("/")
async def create_car():
    pass


@router_car.patch("/")
async def update_car():
    pass
