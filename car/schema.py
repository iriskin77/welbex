from typing import Optional, List

from pydantic import BaseModel


class CreateCarRequest(BaseModel):
    """"Запрос на создание машины"""""

    unique_number: str
    car_name: str
    zip: str
    load_capacity: int


class CreateCarResponse(BaseModel):
    """"Ответ на создание машины"""""

    id: int


class CarUpdateRequest(BaseModel):
    """"Запрос на обновление машины"""""

    unique_number: str
    car_name: str
    zip: str
    load_capacity: int


class CarUpdateResponse(BaseModel):
    """"Ответ на обновление машины"""""

    id: int


class CarGetRequest(BaseModel):
    """"Запрос на получение машины (для CarsGetRequest)"""""

    id: int
    car_name: str
    car_location_id: int
    load_capacity: int
    unique_number: str


class CarsGetRequest(BaseModel):
    """"Запрос на получение списка машин (для грузов)"""""

    cars: List[CarGetRequest]


class CargoCarGetResponse(BaseModel):
    """"Ответ на получение машины"""""

    id: int
    car_name: str
    car_location_id: int
    load_capacity: int
    unique_number: str
    miles: float
