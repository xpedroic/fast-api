from pydantic import BaseModel

# Entidad user
class User(BaseModel):
    id: int | None
    username: str
    email: str