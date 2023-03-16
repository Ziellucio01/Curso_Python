from fastapi import FastAPI
app = FastAPI()


@app.get("/")
async def root():
    return "Hola FastAPI!"

# Url local: https://127.0.0.1:8000


@app.get("/url_moure")
async def url():
    return {"url_curso": "https://mouredev.com/python"}

# Url local: https://127.0.0.1:8000/url_moure

# Inicia el server: python -m uvicorn main:app --reload
# Detener el server CTRL + C

# Documentación con Swagger: https://127.0.0.1:8000/docs
# Documentación con Redocly: htpps://127.0.0.1:8000/redoc
