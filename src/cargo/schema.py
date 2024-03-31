from typing import List
from pydantic import BaseModel, field_validator
from src.location.schema import LocationGetResponse
from src.car.schema import CargoCarGetResponse


class CargoCreateRequest(BaseModel):
    """"Запрос на создание груза"""""

    cargo_name: str
    zip_pickup: int
    zip_delivery: int
    weight: int
    description: str

    @field_validator('weight', mode='before')
    @classmethod
    def check_weight(cls, value):
        if 1 < value < 1000:
            return value


class CargoCreateResponse(BaseModel):
    """"Ответ на создание груза"""""

    id: int


class CargoByIdResponse(BaseModel):
    """"Запрос на получение груза по ID"""""

    cargo_name: str
    weight: int
    description: str
    pick_up_location: LocationGetResponse
    delivery_location: LocationGetResponse
    cars: List[CargoCarGetResponse]


class CargosListResponse(BaseModel):
    """"Запрос на получение списка грузов"""""

    cargos: List[CargoByIdResponse]


class CargoUpdateRequest(BaseModel):
    """"Запрос на обновление груза"""""

    weight: int
    description: str


class CargoUpdateResponse(BaseModel):
    """"Ответ на обновление груза"""""

    id: int


class CargoDeleteResponse(BaseModel):
    """"Ответ на удаление груза"""""

    id: int
