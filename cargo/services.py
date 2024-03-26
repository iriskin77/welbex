from cargo.models import Cargo
from location.models import Location
from cargo.schema import CargoCreateRequest


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









