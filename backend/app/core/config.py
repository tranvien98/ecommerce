import enum
from pathlib import Path
from tempfile import gettempdir
from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """
    version: str = "5.6.2024.1"
    secret_key: str = "ecommerce_backend"
    algorithm: str = "HS256"
    host: str = "0.0.0.0"
    port: int = 5055
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = True

    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO
    # Variables for the database
    db_host: str = "194.233.73.27"
    db_port: int = 17017
    db_name: str = "ecommerce-dev"
    db_user: str = "admin"
    db_password: str = "viendev9z@20024"


    @property
    def mongo_db_url(self):
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return f"mongodb://{quote_plus(self.db_user)}:{quote_plus(self.db_password)}@{self.db_host}:{self.db_port}"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
