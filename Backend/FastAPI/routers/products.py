from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"message": "no encontrado"}}
                   )

products_list = ["Producto 1", "Producto 2",
                 "Producto 3", "Producto 4", "Producto 5"]


@router.get("/")
async def products():
    return products_list


@router.get("/{id}")
async def products_id(id: int):
    return products_list[id]