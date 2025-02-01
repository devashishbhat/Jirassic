#Running the server: uvicorn main:app --host 0.0.0.0 --port 4050

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_routes import user_router
from services.database import get_database
from contextlib import asynccontextmanager

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # "*" allows all domains, or specify a list of allowed domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

db = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle event to initialize and cleanup resources."""
    db = await get_database()  # Initialize the database
    yield  # Continue running the app
    db.client.close()

app.include_router(user_router, prefix="/user")

@app.get("/health-check")
async def heatlh_check():
    return {"status": "Working perfectly fine"}
