from tortoise.expressions import Q
from .models import Cargo
from src.car.models import Car
from src.location.models import Location
from .schema import CargoCreateRequest
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

    cars = await Car.all().select_related("car_location")

    for car in cars:
        miles = count_miles(cargo_latitude=pick_up.latitude,
                            cargo_longitude=pick_up.longitude,
                            car_latitude=car.car_location.latitude,
                            car_longitude=car.car_location.longitude)

        if miles is not None:
            car_item = {"id": car.id,
                        "unique_number": car.unique_number,
                        "car_name": car.car_name,
                        "load_capacity": car.load_capacity,
                        "miles": miles,
                        "car_location": car.car_location}

            list_cars.append(car_item)

    list_cars.sort(key=lambda c: c['miles'])

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
    return list_cargos


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


async def filter_by_weight_or_miles(weight_lt: int, weight_gt: int):
        list_cargos = []
        cargos = await Cargo.all().filter(
            Q(weight__lt=weight_lt) &
            Q(weight__gt=weight_gt))\
            .order_by()

        for cargo in cargos:
            cargo = await get_cargo_cars_by_id(cargo.id)
            list_cargos.append(cargo)

        return list_cargos



# =================== patch/put handlers ===========================


async def update_cargo(id: int, cargo_to_update: dict):
    cargo = await get_cargo_by_id(id=id)
    cargo_to_upd = await cargo.update_from_dict(cargo_to_update)
    await cargo_to_upd.save()
    return cargo_to_upd.id

# ====================delete handlers ==============================


async def delete_cargo_by_id(id: int):
    cargo = await get_cargo_by_id(id=id)
    await cargo.delete()
    return cargo.id





