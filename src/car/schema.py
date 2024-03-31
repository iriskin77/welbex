from typing import Optional, List
from pydantic import BaseModel
from src.location.schema import LocationGetResponse

class CreateCarRequest(BaseModel):
    """"Запрос на создание машины"""""

    unique_number: str
    car_name: str
    zip: int
    load_capacity: int


class CreateCarResponse(BaseModel):
    """"Ответ на создание машины"""""

    id: int


class CarUpdateRequest(BaseModel):
    """"Запрос на обновление машины"""""

    unique_number: Optional[str] = None
    car_name: Optional[str] = None
    zip: Optional[int] = None
    load_capacity: Optional[int] = None


class CarUpdateResponse(BaseModel):
    """"Ответ на обновление машины"""""

    id: int


class CarGetRequest(BaseModel):
    """"Запрос на получение машины (для CarsGetRequest)"""""

    id: int
    car_name: str
    unique_number: str
    load_capacity: int
    car_location: LocationGetResponse


class CarsGetRequest(BaseModel):
    """"Запрос на получение списка машин (для грузов)"""""

    cars: List[CarGetRequest]


class CargoCarGetResponse(BaseModel):
    """"Ответ на получение машины"""""

    id: int
    car_name: str
    unique_number: str
    load_capacity: int
    miles: float
    car_location: LocationGetResponse
