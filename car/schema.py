from pydantic import BaseModel


class CreateCarRequest(BaseModel):

    unique_number: str
    car_name: str
    city: str
    state: str
    latitude: float
    longitude: float
    load_capacity: int
