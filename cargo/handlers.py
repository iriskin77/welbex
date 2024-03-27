from fastapi import APIRouter, HTTPException
from . import services
from .schema import (
                           CargoCreateRequest,
                           CargoCreateResponse,
                           CargosListResponse,
                           CargoByIdResponse,
                           CargoUpdateRequest,
                           CargoUpdateResponse,
                           CargoDeleteResponse
                           )

router_cargo = APIRouter()


@router_cargo.post("/", response_model=CargoCreateResponse)
async def create_cargo(item: CargoCreateRequest):
    """"Создание нового груза (характеристики локаций pick-up, delivery определяются по введенному zip-коду);"""""
    try:
        new_cargo_id = await services.create_cargo(item=item)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return {"id": new_cargo_id}


@router_cargo.get("/{id}")
async def get_cargo_by_id(id: int):
    """"Получение информации о конкретном грузе по ID 
    (локации pick-up, delivery, вес, описание, список номеров ВСЕХ машин с расстоянием до выбранного груза);"""""

    cargo = await services.get_cargo_by_id(id=id)
    if cargo is None:
        raise HTTPException(status_code=404, detail="Cargo with this id was not found")

    try:
        cargo = await services.get_cargo_cars_by_id(id=id)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return cargo


@router_cargo.get("/list_cargos")
async def get_list_cargos():
    """"Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль));"""""
    try:
        cargos = await services.get_cargos_cars()
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return {"cargos": cargos}


@router_cargo.get("/filter")
async def filter_cargos(weight: int):
    """"Фильтр списка грузов (вес, мили ближайших машин до грузов);"""""
    try:
       res = await services.filter_by_weight_or_miles(weight=weight)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return res


@router_cargo.patch("/{id}", response_model=CargoUpdateResponse)
async def update_cargo(id: int, cargo_update: CargoUpdateRequest):
    """Редактирование груза по ID (вес, описание)"""""

    cargo = await services.get_cargo_by_id(id=id)
    if cargo is None:
        raise HTTPException(status_code=404, detail="Cargo with this id was not found")

    cargo_to_update = cargo_update.dict(exclude_none=True)
    if cargo_to_update == {}:
        raise HTTPException(status_code=500, detail="At least one parametre should be provided")

    try:
        cargo_updated_id = await services.update_cargo(id=id, cargo_to_update=cargo_to_update)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return {'id': cargo_updated_id}


@router_cargo.delete("/{id}", response_model=CargoDeleteResponse)
async def delete_cargo(id: int):
    """Удаление груза по ID."""""

    cargo = await services.get_cargo_by_id(id=id)
    if cargo is None:
        raise HTTPException(status_code=404, detail="Cargo with this id was not found")

    try:
        deleted_cargo_id = await services.delete_cargo_by_id(id=id)
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Database error: {ex}")
    return {'id': deleted_cargo_id}
