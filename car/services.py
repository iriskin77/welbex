from car.models import Car
from location.models import Location
from car.schema import CreateCarRequest
from random import randint


async def create_car(car: CreateCarRequest):
    car_loc = await Location.filter(zip=car.zip).first()
    new_car = await Car(unique_number=car.unique_number,
                        car_name=car.car_name,
                        load_capacity=car.load_capacity,
                        car_location=car_loc)

    await new_car.save()
    return new_car.id


async def update_all_cars_location():
    car_locs = await Car.all()
    new_locs = await Location.all()

    for i in range(len(car_locs)):

        rand_location = randint(0, len(new_locs))
        car_locs[i].car_location_id = new_locs[rand_location].id

    await Car.bulk_update(car_locs, ['car_location_id'])


