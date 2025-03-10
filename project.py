
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pathlib import Path

MONGO_URI = "mongodb+srv://yarisster:6p7n5w4E7V1PkvXm@cluster0.yfvax.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "tour_agency"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
tours_collection = db["tours"]

app = FastAPI()

# Добавляем мидлвар для CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Настраиваем шаблоны Jinja2
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# 🔥 Монтируем папку static для подключения CSS и JS
app.mount("/static", StaticFiles(directory="static"), name="static")

class Tour(BaseModel):
    name: str
    description: str
    price: float
    location: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/tours/")
async def create_tour(tour: Tour):
    tour_dict = tour.dict()
    result = await tours_collection.insert_one(tour_dict)
    return {"id": str(result.inserted_id)}

@app.get("/tours/")
async def get_tours():
    tours = await tours_collection.find().to_list(20)
    for tour in tours:
        tour["id"] = str(tour.pop("_id"))  # Преобразуем ObjectId в строку
    return jsonable_encoder(tours)

@app.get("/tours/{tour_id}")
async def get_tour(tour_id: str):
    tour = await tours_collection.find_one({"_id": ObjectId(tour_id)})
    if not tour:
        raise HTTPException(status_code=404, detail="Tour not found")

    tour["id"] = str(tour.pop("_id"))  # Преобразуем ObjectId в строку
    return jsonable_encoder(tour)

@app.put("/tours/{tour_id}")
async def update_tour(tour_id: str, tour: Tour):
    result = await tours_collection.update_one({"_id": ObjectId(tour_id)}, {"$set": tour.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Tour not found")
    return {"message": "Tour updated"}

@app.delete("/tours/{tour_id}")
async def delete_tour(tour_id: str):
    result = await tours_collection.delete_one({"_id": ObjectId(tour_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Tour not found")
    return {"message": "Tour deleted"}