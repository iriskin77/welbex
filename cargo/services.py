from tortoise.expressions import Q
from .models import Cargo
from car.models import Car
from location.models import Location
from .schema import CargoCreateRequest, CargoUpdateRequest
from geopy.distance import geodesic


# =========================== post handlers ===========================


async def create_cargo(item: CargoCreateRequest) -> int:
    pick_up_location, delivery_location = await Location.filter(
        Q(zip=item.zip_pickup) |
        Q(zip=item.zip_delivery)
    )

    new_cargo = await Cargo(cargo_name=item.cargo_name,
                            pick_up_location=pick_up_location,
                            delivery_location=delivery_location,
                            weight=item.weight,
                            description=item.description)
    await new_cargo.save()

    return new_cargo.id


# ============================= get handlers =========================


async def get_cargo_cars_by_id(id: int):
    list_cars = []
    cargo = await get_cargo_by_id(id=id)
    pick_up, delivery = await Location.filter(
        Q(id=cargo.pick_up_location_id) |
        Q(id=cargo.delivery_location_id)
    )
    cars = await Car.all().values()
    for car in cars:
        car_loc = await Location.get(id=car['car_location_id'])
        miles = count_miles(cargo_latitude=pick_up.latitude,
                            cargo_longitude=pick_up.longitude,
                            car_latitude=car_loc.latitude,
                            car_longitude=car_loc.longitude)

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
    list_cargos = []
    cargos = await Cargo.all()
    for cargo in cargos:
        cargo = await get_cargo_cars_by_id(cargo.id)
        list_cargos.append(cargo)
    cargos = {"cargos": list_cargos}
    return cargos


async def get_cargo_by_id(id: int):
    cargo = await Cargo.get_or_none(id=id)
    if cargo is not None:
        return cargo


def count_miles(cargo_latitude: float,
                cargo_longitude: float,
                car_latitude: float,
                car_longitude: float):

    cargo = (cargo_latitude, cargo_longitude)
    car = (car_latitude, car_longitude)

    miles = geodesic(cargo, car).miles

    if miles <= 450:
        return miles


async def filter_by_weight_or_miles(weight: int):
        list_cargos = []
        cargos = await Cargo.all().filter(Q(weight__lt=weight)).order_by()
        for cargo in cargos:
            cargo = await get_cargo_cars_by_id(cargo.id)
            list_cargos.append(cargo)
        return list_cargos



# =================== patch/put handlers ===========================


async def update_cargo(id: int, cargo_to_update: dict):
    cargo = await get_cargo_by_id(id=id)
    cargo = await cargo.update_from_dict(cargo_to_update).save()
    return cargo.id

# ====================delete handlers ==============================


async def delete_cargo_by_id(id: int):
    cargo = await get_cargo_by_id(id=id)
    await cargo.delete()
    return cargo.id





