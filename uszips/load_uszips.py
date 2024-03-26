import pandas as pd
from pandas import DataFrame
from location.models import Location
import asyncio
from core.settings import DATABASE_URI


uszips = pd.read_csv("/home/abc/Рабочий стол/welbex/uszips/uszips.csv")


async def load_uszips(uszips: DataFrame) -> None:
    uszips_to_add = uszips[["zip","latitude","longitude","city","state"]]
    print(uszips_to_add.to_dict('records'))
    await Location.bulk_create([Location(**item) for item in uszips_to_add.to_dict('records')])




