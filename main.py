from fastapi import FastAPI
import uvicorn
from routes import routes
from tortoise.contrib.fastapi import register_tortoise
from core.settings import DATABASE_URI, engine
from core.async_session import get_async_session
from contextlib import asynccontextmanager
import pandas as pd
from location.models import Location
from pandas import DataFrame


uszips = pd.read_csv("/home/abc/Рабочий стол/welbex/uszips/uszips.csv")


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     uszips_to_add = uszips[["zip","latitude","longitude","city","state"]]
#     async with engine.begin() as conn:
#         #conn = await conn.connection()
#         c = await conn.run_sync()
#         uszips_to_add.to_sql("location", c)
#         # await conn.run_sync(
#         #     lambda sync_conn: uszips_to_add.to_sql(
#         #         "location",
#         #         #con=sync_conn,
#         #     ),
#         # )
#         await c.commit()
#     yield
    # uszips_to_add = uszips[["zip","latitude","longitude","city","state"]]
    # uszips_to_add.to_sql("location", engine)
    # yield




app = FastAPI(lifespan=lifespan)
app.include_router(routes)



