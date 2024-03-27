from car.models import Car
from location.models import Location
from random import randint


async def update_all_cars_location() -> None:
    car_locs = await Car.all()
    new_locs = await Location.all()

    for i in range(len(car_locs)):

        rand_location = randint(0, len(new_locs))
        car_locs[i].car_location_id = new_locs[rand_location].id

    await Car.bulk_update(car_locs, ['car_location_id'])
