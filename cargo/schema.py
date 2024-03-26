from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from location.schema import Location
from car.schema import CreateCarRequest


class CargoCreateRequest(BaseModel):

    cargo_name: str
    zip_pickup: str
    zip_delivery: str
    weight: int
    description: str


class CargoCreateResponse(CargoCreateRequest):

    created_at: datetime
    pick_up_location: Location
    delivery_location: Location


class CargoCarsResponse(CargoCreateRequest):

    cars: Optional[CreateCarRequest]


class CargoUpdateRequest(BaseModel):

    weight: int
    description: str
