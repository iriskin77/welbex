from random import choice
from src.car.models import Car
from src.location.models import Location


async def update_all_cars_location() -> None:
    """"Автоматическое обновление локаций всех машин раз в 3 минуты (локация меняется на другую случайную)"""""
    car_locs_to_update = await Car.all()
    new_locs_to_update = await Location.all()

    for i in range(len(car_locs_to_update)):

        location_to_update = choice(new_locs_to_update)
        car_locs_to_update[i].car_location_id = location_to_update.id

    await Car.bulk_update(car_locs_to_update, ['car_location_id'])
