from fastapi import APIRouter, HTTPException, status
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_shema

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


users_list = []


@ router.get("/", response_model=list(User))
async def users():
    return users_shema(db_client.local.users.find())

# Path


@ router.get("/{ide}")
async def user(ide: int):
    return searh_user("_id", user.email)

# Query http://127.0.0.1:8000/user/?id=1


@ router.get("/")
async def userget():
    return db_client.local.users.find()


@ router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user_post(user: User):
    if type(searh_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="El usuario ya existe")

    user_dict = dict(user)
    del user_dict["id"]
    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.users.find_one({"_id": id}))

    return User(**new_user)


@ router.put("/")
async def user_put(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No se ha actualizado el usario")
        # return {"error": "No se ha actualizado el usuario"}
    else:
        return user


@router.delete("/{id}")
async def user_del(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return {"mensaje": "El usuario se elimino correctamente"}

    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No se ha eliminado el usuario")
        # return {"error": "No se ha eliminado el usuario"}


def searh_user(field: str, key: str):
    try:
        user = db_client.local.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se ha encontrado el usuario"}
