from fastapi import FastAPI
import uvicorn
from routes import routes
from tortoise.contrib.fastapi import register_tortoise
from core.settings import DATABASE_URI, APPS_MODELS
from contextlib import asynccontextmanager
import pandas as pd
from location.models import Location
from pandas import DataFrame


uszips = pd.read_csv("/home/abc/Рабочий стол/welbex/uszips/uszips.csv")





app = FastAPI()
app.include_router(routes)


register_tortoise(
    app=app,
    db_url=DATABASE_URI,
    modules={"models": APPS_MODELS},
    generate_schemas=False,
    add_exception_handlers=False,
)



if __name__ == '__main__':
    uvicorn.run(app=app, port=7777)
