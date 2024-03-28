from typing import Optional, List

from pydantic import BaseModel


class CreateCarRequest(BaseModel):

    unique_number: str
    car_name: str
    zip: str
    load_capacity: int


class CreateCarResponse(BaseModel):

    id: int


class CarUpdateRequest(BaseModel):

    unique_number: str
    car_name: str
    zip: str
    load_capacity: int


class CarUpdateResponse(BaseModel):

    id: int


class CarGetRequest(BaseModel):

    id: int
    car_name: str
    car_location_id: int
    load_capacity: int
    unique_number: str


class CarsGetRequest(BaseModel):

    cars: List[CarGetRequest]


class CargoCarGetResponse(BaseModel):

    id: int
    car_name: str
    car_location_id: int
    load_capacity: int
    unique_number: str
    miles: float
