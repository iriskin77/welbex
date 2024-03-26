from fastapi import APIRouter
from cargo.handlers import router_cargo


routes = APIRouter()

routes.include_router(router=router_cargo, prefix="/cargo")
