from .models import Location
import pandas as pd
from src.core import settings


async def get_uszips(limit: int):
    locations = await Location.all().limit(limit)
    return locations


async def load_uszips() -> None:
    uszips = pd.read_csv(settings.USZIPS_PATH)
    uszips_to_add = uszips[["zip", "latitude", "longitude", "city", "state"]]
    await Location.bulk_create([Location(**item) for item in uszips_to_add.to_dict('records')])


async def get_location_by_zip(zip: int):
    location = await Location.get_or_none(zip=zip)
    if location is not None:
        return location
