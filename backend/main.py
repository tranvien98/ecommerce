import uvicorn
from app.core.config import settings


def main():
    """
    Application entry point.
    """
    uvicorn.run(
        "app.core.application:get_app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        workers=settings.workers_count,
        factory=True
    )

if __name__ == "__main__":
    main()
