from pydantic import BaseModel
from datetime import datetime


class Location(BaseModel):

    city: str
    state: str
    zip: int
    latitude: float
    longitude: float
    created_at: datetime




