from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from .schema import CreateCarRequest, CreateCarResponse, CarUpdateRequest, CarUpdateResponse, CarsGetRequest
from . import services
from location.services import get_location_by_zip


router_car = APIRouter()


@router_car.post("/", response_model=CreateCarResponse)
async def create_car(car: CreateCarRequest):
    """"Создание машины"""""
    try:
        new_car_id = await services.create_car(car=car)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return {"id": new_car_id}


@router_car.patch("/{id}", response_model=CarUpdateResponse)
async def update_car_by_id(id: int, car_update: CarUpdateRequest):
    """"Редактирование машины по ID (локация (определяется по введенному zip-коду))"""""

    car = await services.get_car_by_id(id=id)
    if car is None:
        raise HTTPException(status_code=404, detail="Cargo with this id was not found")

    car_to_update = car_update.dict(exclude_none=True)
    if car_to_update == {}:
        raise HTTPException(status_code=500, detail="At least one parametre should be provided")

    if car_update.zip is not None:
        location = await get_location_by_zip(zip=car_update.zip)
        if location is None:
            raise HTTPException(status_code=404, detail="This location (zip) was not found")
    try:
        print(car_to_update)
        car_updated_id = await services.update_car_by_id(id=id, car_to_update=car_to_update)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return {"id": car_updated_id}


@router_car.post("/upload_cars")
async def upload_cars():
    """"Добавляет 200 случайных машин в БД"""""
    try:
        await services.load_cards()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return JSONResponse({"cars uploaded successfully": 201})


@router_car.get("{id}")
async def get_car(id: int):
    try:
        car = await services.get_car_by_id(id=id)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return car


@router_car.get("/get_cars", response_model=CarsGetRequest)
async def get_cars(limit: int | None = None):
    """"Получение списка машин"""""
    try:
        cars = await services.get_cars(limit=limit)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return {"cars": cars}
