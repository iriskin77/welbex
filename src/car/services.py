from random import choice, randint
from string import ascii_uppercase
from .models import Car
from src.location.models import Location
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

    if "zip" not in car_to_update:
        await car.update_from_dict(car_to_update)
        await car.save()
        return car.id
    else:
        new_car_location = await Location.get(zip=car_to_update['zip'])
        car_to_update['car_location_id'] = new_car_location.id
        await car.update_from_dict(car_to_update)
        await car.save()
        return car.id


async def get_cars(limit: int):
    cars = await Car.all().select_related("car_location").limit(limit).order_by("id")
    res = []
    for car in cars:
        car_item = {
            "id": car.id,
            "car_name": car.car_name,
            "unique_number": car.unique_number,
            "load_capacity": car.load_capacity,
            "car_location": car.car_location,
        }
        res.append(car_item)

    return res


async def load_cards() -> None:
    cars = await generate_cars()
    await Car.bulk_create([Car(**car) for car in cars])


async def generate_cars() -> list:
    locations = await Location.all()

    cars = []

    for i in range(200):
        car = {}
        rand_letter = choice([letter for letter in ascii_uppercase])
        rand_int = randint(1000, 9999)
        unique_number = str(rand_int) + rand_letter
        weight_capacity = randint(1, 1000)
        car_name = "car_name" + str(randint(1, 9999))
        car['unique_number'] = unique_number
        car['car_name'] = car_name
        car['load_capacity'] = weight_capacity
        car['car_location_id'] = locations[i].id
        cars.append(car)

    return cars
