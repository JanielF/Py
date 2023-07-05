from fastapi import FastAPI

app = FastAPI() #creamos variable para almacenar la clase de FastAPI.

@app.get("/") #raiz de la IP de donde se despliega la API (localhost)
async def root():  #Async PERMITE QUE CONTINUE SUS OPERACIONES JUNTO CON OTRAS OPERACIONES.
    return ("Hola FastAPI, es todo un placer")

#python -m uvicorn main:app --reload con CTRL C se puee apagar el server local.

@app.get("/url") #http://127.0.0.1:8000/url
async def url():
    return {"url":"https://mouredev.com/pyhon"}