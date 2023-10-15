from fastapi import FastAPI
from routers import products, users, users_db
from fastapi.staticfiles import StaticFiles

# Url Local: http://127.0.0.1:8000
# Start Server: uvicorn main:app --reload
# Stop Server: Ctrl + C

# Documentacion: http://127.0.0.1:8000/docs

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(users_db.router)
app.mount("/images", StaticFiles(directory="images"), name="images")

@app.get("/")
async def root():
    return "Hola"

@app.get("/url")
async def url():
    return {"url": "https://www.google.com"}