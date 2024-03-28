from .models import Location


async def get_uszips(limit: int):
    locations = await Location.all().limit(limit)
    return locations
