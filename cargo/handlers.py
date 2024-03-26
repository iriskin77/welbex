from fastapi import APIRouter, Depends, HTTPException
from cargo.schema import CargoCreateRequest, CargoCreateResponse
from cargo import services


router_cargo = APIRouter()


@router_cargo.post("/")
async def create_cargo(item: CargoCreateRequest):
    """"Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);"""""
    res = await services.create_cargo(item=item)
    return res


@router_cargo.get("/list_cargos")
async def get_list_cargos():
    """"Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль));"""""
    pass


@router_cargo.get("get_cargo")
async def get_cargo_by_id():
    """"Получение информации о конкретном грузе по ID 
    (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза);"""""
    pass


@router_cargo.put("/")
async def update_cargo():
    """Редактирование груза по ID (вес, описание)"""""
    pass


@router_cargo.delete("/")
async def delete_cargo():
    """Удаление груза по ID."""""
    pass
