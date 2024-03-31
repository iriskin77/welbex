from typing import List
from pydantic import BaseModel
from datetime import datetime


class Location(BaseModel):

    state: str
    zip: int
    latitude: float
    longitude: float
    state: str
    city: str
    created_at: datetime
    id: int


class LocationGetResponse(BaseModel):
    """Ответ на получение локации (для LocationListResponse)"""""

    id: int
    state: str
    zip: int
    city: str
    latitude: float
    longitude: float
    created_at: datetime


class LocationListResponse(BaseModel):
    """Ответ на получение списка локаций"""""

    locations: List[LocationGetResponse]
