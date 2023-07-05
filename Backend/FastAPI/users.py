from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#python -m uvicorn users:app --reload

#Entidad user
class User(BaseModel): #BaseModel da la capacidad de crear una entidad.
    name: str
    surname: str
    url: str
    age: int

users_list = [User(name = "Janiel", surname= "Flores", url = "https://janiel.dev", age = 19),
            User(name = "Arianna", surname= "Flores", url = "https://arianna.dev", age = 22),
            User(name= "Melanie", surname= "Ureña", url= "https://melanie.dev", age= 19)]

@app.get("/usersjson") 
async def usersjson():  
    return [{"name": "Janiel", "surname": "Flores", "url":"https://janiel.dev", "age": 19},
            {"name": "Arianna", "surname": "Flores", "url":"https://arianna.dev", "age": 22},
            {"name": "Melanie", "surname": "Ureña", "url":"https://melanie.dev", "age": 19}]

@app.get("/users")
async def users():
    return users_list