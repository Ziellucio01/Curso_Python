from fastapi import FastAPI
from routers import products, users, basic_auth_user, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles
app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
# app.include_router(basic_auth_user.router) # api sin incriptacion de datos
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return "Hola FastAPI!"

# Url local: https://127.0.0.1:8000


@app.get("/url")
async def url():
    return {"url_curso": "https://mouredev.com/python"}

# Url local: https://127.0.0.1:8000/url_moure

# Inicia el server: python -m uvicorn main:app --reload
# Detener el server CTRL + C

# Documentación con Swagger: https://127.0.0.1:8000/docs
# Documentación con Redocly: htpps://127.0.0.1:8000/redoc
