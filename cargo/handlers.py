from fastapi import APIRouter, Depends, HTTPException
from cargo.schema import CargoCreateRequest, CargoCreateResponse
from cargo.models import Cargo
from car.models import Car
from cargo import services


router_cargo = APIRouter()


@router_cargo.post("/")
async def create_cargo(item: CargoCreateRequest):
    """"Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);"""""
    try:
        res = await services.create_cargo(item=item)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return res


@router_cargo.get("/list_cargos")
async def get_list_cargos():
    """"Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль));"""""
    try:
        res = await services.get_cargos_cars()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return res


@router_cargo.get("/get_cargo")
async def get_cargo_by_id(id: int):
    """"Получение информации о конкретном грузе по ID 
    (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза);"""""

    cargo = await services.get_cargo_by_id(id=id)
    if cargo is None:
        raise HTTPException(status_code=404, detail="Cargo with this id was not found")

    try:
        res = await services.get_cargo_cars_by_id(id=id)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return res


@router_cargo.get("/filter")
async def filter_cargos(weight: int):
    """"Фильтр списка грузов (вес, мили ближайших машин до грузов);"""""
    try:
       res = await services.filter_by_weight_or_miles(weight=weight)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return res


@router_cargo.patch("/")
async def update_cargo():
    """Редактирование груза по ID (вес, описание)"""""
    pass


@router_cargo.delete("/")
async def delete_cargo():
    """Удаление груза по ID."""""
    pass
