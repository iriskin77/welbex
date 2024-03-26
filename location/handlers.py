from fastapi import APIRouter, Depends, HTTPException
from cargo import services
import pandas as pd
from pandas import DataFrame
from location.models import Location

router_location = APIRouter()

uszips = pd.read_csv("/home/abc/Рабочий стол/welbex/uszips/uszips.csv")


@router_location.get("/")
async def load_uszips():
    uszips_to_add = uszips[["zip","latitude","longitude","city","state"]]
    #print(uszips_to_add.to_dict('records'))
    for i in uszips_to_add.to_dict('records'):
        print(i)
        await Location.create(**i)
    #
    # await Location.bulk_create(uszips_to_add.to_dict('records'))

    return 1

