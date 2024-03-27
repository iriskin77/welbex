from random import randint
from car.models import Car
from location.models import Location


async def update_all_cars_location() -> None:
    car_locs_to_update = await Car.all()
    new_locs_to_update = await Location.all()

    for i in range(len(car_locs_to_update)):

        rand_location = randint(0, len(new_locs_to_update)-1)
        car_locs_to_update[i].car_location_id = new_locs_to_update[rand_location].id

    await Car.bulk_update(car_locs_to_update, ['car_location_id'])
