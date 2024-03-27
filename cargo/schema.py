from typing import List
from pydantic import BaseModel
from location.schema import Location
from car.schema import CreateCarRequest

# create_cargo

class CargoCreateRequest(BaseModel):
    """"Запрос на создание груза"""""

    cargo_name: str
    zip_pickup: str
    zip_delivery: str
    weight: int
    description: str


class CargoCreateResponse(BaseModel):
    """"Ответ на создание груза"""""

    id: int

# get_list_cargos


class CargoByIdResponse(BaseModel):

    cargo_name: str
    weight: int
    description: str
    pick_up_location: Location
    delivery_location: Location
    cars: List[CreateCarRequest]


class CargosListResponse(BaseModel):

    cargos: List[CargoByIdResponse]


class CargoUpdateRequest(BaseModel):

    weight: int
    description: str


class CargoUpdateResponse(BaseModel):

    id: int


class CargoDeleteResponse(BaseModel):

    id: int
