from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# Url Local: http://127.0.0.1:8000
# Start Server: uvicorn users:app --reload
# Stop Server: Ctrl + C

# Documentacion: http://127.0.0.1:8000/docs

router = APIRouter(tags=["users"])

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int

users_list = [User(id=1, name="Pedro", surname="Izquierdo", email="pedro@gmail.com", age=25),
         User(id=2, name="Alvaro", surname="Apio", email="apio@gmail.com", age=26),
         User(id=3, name="Kiko", surname="Morales", email="kiko@gmail.com", age=27)]

    

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Pedro","surname": "Izquierdo", "email": "pedro@gmail.com", "age": 25},
            {"name": "Alvaro","surname": "Apio", "email": "apio@gmail.com", "age": 26},
            {"name": "Kiko","surname": "Morales", "email": "kiko@gmail.com", "age": 26}]


@router.get("/users")
async def users():
    return users_list

#Path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#Query
@router.get("/user/")
async def user(id: int):
    return search_user(id)


@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_list.append(user)
        return users_list


@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return users_list
    

@router.delete("/user/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}
    else:
        return users_list


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    

 
