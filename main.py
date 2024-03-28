from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from routes import routes
from core import settings
from tortoise.contrib.fastapi import register_tortoise
from car.tasks import update_all_cars_location
import uvicorn


app = FastAPI()
app.include_router(routes)


@app.on_event('startup')
async def init_data():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_all_cars_location, 'cron', minute='*/3')
    scheduler.start()


register_tortoise(
    app=app,
    db_url=settings.DATABASE_URI,
    modules={"models": settings.APPS_MODELS},
    generate_schemas=False,
    add_exception_handlers=False,
)




if __name__ == '__main__':
    uvicorn.run(app=app, port=7777)
