from .models import Car
from location.models import Location
from .schema import CreateCarRequest


async def create_car(car: CreateCarRequest) -> int:
    car_loc = await Location.filter(zip=car.zip).first()
    new_car = await Car(unique_number=car.unique_number,
                        car_name=car.car_name,
                        load_capacity=car.load_capacity,
                        car_location=car_loc)

    await new_car.save()
    return new_car.id


async def get_car_by_id(id: int):
    car = await Car.get_or_none(id=id)
    if car is not None:
        return car


async def update_car_by_id(id: int, car_to_update: dict):
    car = await get_car_by_id(id=id)
    new_car_location = await Location.get(zip=car_to_update['zip'])
    car_to_update['car_location_id'] = new_car_location.id
    await car.update_from_dict(car_to_update).save()
    return car.id


async def get_cars(limit: int):
    cars = await Car.all().limit(limit)
    return cars
