from contextlib import asynccontextmanager

from app.databases import init_mongo_db
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the db
    await init_mongo_db()
    print("Startup complete")
    yield
    print("Shutdown complete")
