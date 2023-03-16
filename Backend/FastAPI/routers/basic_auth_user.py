from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool


class UserDB(User):
    password: str


users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "braismoure@mourede.com",
        "disable": False,
        "password": "123456"
    },
    "mouredev2": {
        "username": "mouredev2",
        "full_name": "Brais Moure 2",
        "email": "braismoure2@mourede.com",
        "disable": True,
        "password": "654321"
    }
}


def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    pass
