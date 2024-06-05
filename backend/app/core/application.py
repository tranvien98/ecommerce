from pathlib import Path

from app.core.lifetime import lifespan
from app.core.middleware import AuthMiddleware
from app.core.routers import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse

APP_ROOT = Path(__file__).parent.parent

DESCRIPTION = """
This API for ecommerce platform.
"""

def get_app() -> FastAPI:
    """
    Create FastAPI application.

    :return: FastAPI application.
    """

    app = FastAPI(
        title="Ecommerce API",
        description=DESCRIPTION,
        version="0.1.1",
        lifespan=lifespan,
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.add_middleware(AuthMiddleware)
    app.include_router(router, prefix="/api")



    return app
