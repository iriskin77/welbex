from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from routes import routes
from core import settings
from tortoise.contrib.fastapi import register_tortoise
from car.tasks import update_all_cars_location


app = FastAPI()
app.include_router(routes)


@app.on_event('startup')
async def update_cars_locations():
    """"Автоматическое обновление локаций всех машин раз в 3 минуты (локация меняется на другую случайную)."""""
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
