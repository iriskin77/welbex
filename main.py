from fastapi import FastAPI, BackgroundTasks
from routes import routes
from tortoise.contrib.fastapi import register_tortoise
from core.settings import DATABASE_URI, APPS_MODELS
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import pandas as pd
from tasks import update_all_cars_location



app = FastAPI()
app.include_router(routes)


@app.on_event('startup')
async def init_data():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_all_cars_location, 'cron', minute='*/3')
    scheduler.start()


register_tortoise(
    app=app,
    db_url=DATABASE_URI,
    modules={"models": APPS_MODELS},
    generate_schemas=False,
    add_exception_handlers=False,
)



if __name__ == '__main__':
    uvicorn.run(app=app, port=7777)
