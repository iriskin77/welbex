from fastapi import APIRouter
from cargo.handlers import router_cargo
from car.handlers import router_car


routes = APIRouter()

routes.include_router(router=router_cargo, prefix="/cargo")
routes.include_router(router=router_car, prefix="/car")
