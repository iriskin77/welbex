import pandas as pd
from location.models import Location
from car.models import Car
from random import randint
from string import ascii_uppercase


uszips = pd.read_csv("/home/abc/Рабочий стол/welbex/load_data/uszips.csv")


async def load_uszips(uszips: pd.DataFrame) -> None:
    uszips_to_add = uszips[["zip","latitude","longitude","city","state"]]
    await Location.bulk_create([Location(**item) for item in uszips_to_add.to_dict('records')])


async def load_cards() -> None:
    cars = await generate_cars()
    await Car.bulk_create([Car(**car) for car in cars])


async def generate_cars() -> list:
    locs = await Location.all()

    cars = []

    for i in range(2000):
        car = {}
        rand_letter = ascii_uppercase[randint(0, len(ascii_uppercase)-1)]
        rand_int = randint(1000, 9999)
        unique_number = str(rand_int) + rand_letter
        weight_capacity = randint(0, 1000)
        car_name = "car_name" + str(randint(1, 2000))
        car['unique_number'] = unique_number
        car['car_name'] = car_name
        car['load_capacity'] = weight_capacity
        car['load_capacity'] = locs[i].id
        cars.append(car)

    return cars



