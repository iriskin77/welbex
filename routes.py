from fastapi import APIRouter
from cargo.handlers import router_cargo
from car.handlers import router_car
from location.handlers import router_location


routes = APIRouter()

routes.include_router(router=router_cargo, prefix="/cargo")
routes.include_router(router=router_car, prefix="/car")
routes.include_router(router=router_location, prefix="/location")
