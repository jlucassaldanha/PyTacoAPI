from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.src.repository.json_store import TacoJsonRepository
from api.src.routers import food

@asynccontextmanager
async def lifespan(app: FastAPI):
    json_path = "api/data/taco_cleaned.json"
    TacoJsonRepository.load_data(json_path)

    yield

app = FastAPI(
    title="PyTACOAPI",
    description="API de consulta de macronutrientes servida em memória.",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(food.router, prefix="api/v1")