from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from .schema import CreateCarRequest, CarUpdateRequest
from . import services
from car.models import Car
from location.models import Location
from load_data import load

router_car = APIRouter()


@router_car.post("/")
async def create_car(car: CreateCarRequest):
    try:
        new_car_id = await services.create_car(car=car)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return new_car_id


@router_car.patch("/{id}")
async def update_car_by_id(id: int, car_update: CarUpdateRequest):
    """"Редактирование машины по ID (локация (определяется по введенному zip-коду))"""

    car = await services.get_car_by_id(id=id)
    if car is None:
        raise HTTPException(status_code=404, detail="Cargo with this id was not found")

    car_to_update = car_update.dict(exclude_none=True)
    if car_to_update == {}:
        raise HTTPException(status_code=500, detail="At least one parametre should be provided")

    try:
        car_updated_id = await services.update_car_by_id(id=id, car_to_update=car_to_update)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return {"id": car_updated_id}


@router_car.get("/upload_cars")
async def upload_cars():
    """"Добавляет 400 случайных машин в БД"""""
    try:
        await load.load_cards()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return JSONResponse({"cars uploaded successfully": 201})


@router_car.get("/")
async def get_cars(limit: int):
    try:
        cars = await services.get_cars(limit=limit)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return cars


# @router_car.get("/select_related")
# async def test():
#     cars = await Car.all().values()
#     cars_id = [car_id['car_location_id'] for car_id in cars]
#     res = await Location.filter(id__in=cars_id)
#     return res

