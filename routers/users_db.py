from fastapi import APIRouter, HTTPException
from db.models.user import User
from db.schemas.user import user_schema
from db.client import db_client

router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={404: {"message": "No encontrado"}})


users_list = []


@router.get("/")
async def userdb():
    return users_list

#Path
@router.get("/{id}")
async def user(id: int):
    return search_user(id)

#Query
@router.get("/")
async def user(id: int):
    return search_user(id)


@router.post("/", status_code=201)
async def userdb(user: User):
    #if type(search_user(user.id)) == User:
    #   raise HTTPException(status_code=404, detail="El usuario ya existe")
    #else:

    user_dict = dict(user)
    del user_dict["id"]
    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.users.find_one({"_id": id}))

    return User(**new_user)


@router.put("/")
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
    

@router.delete("/{id}")
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
    

 
