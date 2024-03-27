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
