import pandas as pd
from pandas import DataFrame
from location.models import Location
import asyncio


uszips = pd.read_csv("/home/abc/Рабочий стол/welbex/uszips/uszips.csv")


async def load_uszips(uszips: DataFrame):
    uszips_to_add = uszips[["zip","lat","lng","city","state_name"]]
    #print(uszips_to_add.to_dict('records'))
    for i in uszips_to_add.to_dict('records'):
        await Location(**i)
        await Location.save()

    #await Location.bulk_create(uszips_to_add.to_dict('records'))


