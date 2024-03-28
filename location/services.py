from .models import Location
import pandas as pd
from core import settings


async def get_uszips(limit: int):
    locations = await Location.all().limit(limit)
    return locations


async def load_uszips() -> None:
    uszips = pd.read_csv(settings.USZIPS_PATH)
    uszips_to_add = uszips[["zip", "latitude", "longitude", "city", "state"]]
    await Location.bulk_create([Location(**item) for item in uszips_to_add.to_dict('records')])
