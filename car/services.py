from car.models import Car
from car.schema import CreateCarRequest


async def create_car(car: CreateCarRequest):
    new_car = await Car(**car.dict())
    await new_car.save()
    return new_car.id



