from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev",
                "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]


@app.get("/users")
async def users():
    return users_list

# Path


@app.get("/user/{ide}")
async def user(ide: int):
    return searh_user(ide)

# Query http://127.0.0.1:8000/user/?id=1


@app.get("/user/")
async def user(id: int):
    return searh_user(id)


@app.post("/user/")
async def user(user: User):
    if type(searh_user(user.id)) == User:
        return {"error": "El usuario ya existe"}
    else:
        users_list.append(user)
        return user


@app.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user


@app.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return {"mensaje": "El usuario se elimin correctamente"}

    if not found:
        return {"error": "No se ha eliminado el usuario"}


def searh_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
