from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["users"])


# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
              User(id=2, name="Moure", surname="Dev",
                   url="https://mouredev.com", age=35),
              User(id=3, name="Haakon", surname="Dahlberg", url="https://haakon.com", age=35)]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev",
                "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]


@router.get("/users")
async def users():
    return users_list

# Path


@router.get("/user/{ide}")
async def user(ide: int):
    return searh_user(ide)

# Query http://127.0.0.1:8000/user/?id=1


@router.get("/user/")
async def userget(id: int):
    return searh_user(id)


@router.post("/user/", response_model=User, status_code=201)
async def user_post(user: User):
    if type(searh_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
        # return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return user


@router.put("/user/")
async def user_put(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        raise HTTPException(
            status_code=404, detail="No se ha actualizado el usario")
        # return {"error": "No se ha actualizado el usuario"}
    else:
        return user


@router.delete("/user/{id}")
async def user_del(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return {"mensaje": "El usuario se elimino correctamente"}

    if not found:
        raise HTTPException(
            status_code=404, detail="No se ha eliminado el usuario")
        # return {"error": "No se ha eliminado el usuario"}


def searh_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
