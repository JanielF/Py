from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#python -m uvicorn users:app --reload

#Entidad user
class User(BaseModel): #BaseModel da la capacidad de crear una entidad.
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id= 1, name = "Janiel", surname= "Flores", url = "https://janiel.dev", age = 19),
            User(id= 2, name = "Arianna", surname= "Flores", url = "https://arianna.dev", age = 22),
            User(id= 3, name= "Melanie", surname= "Ureña", url= "https://melanie.dev", age= 19)]

@app.get("/usersjson") 
async def usersjson():  
    return [{"name": "Janiel", "surname": "Flores", "url":"https://janiel.dev", "age": 19},
            {"name": "Arianna", "surname": "Flores", "url":"https://arianna.dev", "age": 22},
            {"name": "Melanie", "surname": "Ureña", "url":"https://melanie.dev", "age": 19}]

@app.get("/users")
async def users():
    return users_list

#Path
@app.get("/user/{id}")
async def user(id: int):
    return searh_user(id)

#Query
@app.get("/user/")
async def user(id: int):
    return searh_user(id)

#POST
@app.post("/user/")
async def user(user: User):
    if type(searh_user(user.id)) == User:
        return {"error": "Usuario ya Existente"}
    else:
        users_list.append(user)
        return user

#PUT
@app.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return{"erorr":"No se ha actualizado el usuario"}
    else:
        return user

#DELETE
@app.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se a encontrado el usuario"}


def searh_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuaruo"}

