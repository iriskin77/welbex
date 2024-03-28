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

    longitude: float
    state: str
    id: int
    zip: int
    city: str
    latitude: float
    created_at: datetime


class LocationListResponse(BaseModel):
    """Ответ на получение списка локаций"""""

    locations: List[LocationGetResponse]
