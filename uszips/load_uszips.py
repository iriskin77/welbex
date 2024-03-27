import pandas as pd
from pandas import DataFrame
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from core.async_session import get_async_session
from location.models import Location
from functools import partial
import asyncio
from core.settings import DATABASE_URI, engine


uszips = pd.read_csv("/home/abc/Рабочий стол/welbex/uszips/uszips.csv")


async def load_uszips(uszips: DataFrame) -> None:
    uszips_to_add = uszips[["zip","latitude","longitude","city","state"]]
    print(uszips_to_add.to_dict('records'))
    await Location.bulk_create([Location(**item) for item in uszips_to_add.to_dict('records')])


async def write_sql(engine):
   uszips_to_add = uszips[["zip","latitude","longitude","city","state"]]
   #SessionLocal = sessionmaker(autoflush=False, bind=engine, class_=AsyncSession)
   async with get_async_session() as conn:
    #session = get_async_session()
       conn.bulk_save_objects([Location(**item) for item in uszips_to_add.to_dict('records')])
       conn.commit()


asyncio.run(write_sql(engine))





