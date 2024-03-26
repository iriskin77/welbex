from tortoise.expressions import Q

from cargo.models import Cargo
from car.models import Car
from location.models import Location
from cargo.schema import CargoCreateRequest
from geopy.distance import geodesic


# =========================== post handlers ===========================


async def create_cargo(item: CargoCreateRequest):
    pick_up_location = await Location.filter(zip=item.zip_pickup).first()
    delivery_location = await Location.filter(zip=item.zip_delivery).first()

    print(pick_up_location)
    print(delivery_location)

    new_cargo = await Cargo(cargo_name=item.cargo_name,
                            pick_up_location=pick_up_location,
                            delivery_location=delivery_location,
                            weight=item.weight,
                            description=item.description)
    await new_cargo.save()

    return new_cargo.id


# ============================= get handlers =========================


def count_miles(cargo_latitude: float,
                cargo_longitude: float,
                car_latitude: float,
                car_longitude: float):

    cargo = (cargo_latitude, cargo_longitude)
    car = (car_latitude, car_longitude)

    miles = geodesic(cargo, car).miles

    if miles <= 450:
        return miles


async def get_cargo_cars_by_id(id: int):
    list_cars = []
    cargo = await get_cargo_by_id(id=id)
    pick_up, delivery = await Location.filter(
        Q(id=cargo.pick_up_location_id) |
        Q(id=cargo.delivery_location_id)
    )
    cars = await Car.all().values()
    for car in cars:
        miles = count_miles(cargo_latitude=pick_up.latitude,
                            cargo_longitude=pick_up.longitude,
                            car_latitude=car['latitude'],
                            car_longitude=car['longitude'])
        if miles is not None:
            car['miles'] = miles
            list_cars.append(car)

    res = {"cargo_name": cargo.cargo_name,
           "weight": cargo.weight,
           "description": cargo.description,
           "pick_up_location": pick_up,
           "delivery_location": delivery,
           "cars": list_cars}

    return res


async def get_cargos_cars():
    res = []
    cargos = await Cargo.all()
    for cargo in cargos:
        r = await get_cargo_cars_by_id(cargo.id)
        res.append(r)
    return res


async def get_cargo_by_id(id: int):
    cargo = await Cargo.get_or_none(id=id)
    if cargo is not None:
        return cargo


# =================== patch/put handlers ===========================


# ====================delete handlers ==============================

async def delete_cargo_by_id(id: int):
    cargo = await Cargo.filter(id=id).first()
    await cargo.delete()
    return cargo.id





