import logging
import secrets
from enum import Enum
from typing import Union

from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, validator, RedisDsn

from app.db.enum import Flavors

load_dotenv()


class Environment(str, Enum):
    development = "development"
    production = "production"
    staging = "staging"
    testing = "testing"


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    STALE_TIME: int = 10  # seconds for stale data

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, list[str]]) -> Union[list[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str

    TEST_USER: str
    TEST_USER_PASSWORD: str
    ENVIRONMENT: Environment = Environment.development
    DATABASE_FLAVOR: Flavors
    SQLALCHEMY_DATABASE_URI: str | None = None

    REDIS_DSN: RedisDsn = "redis://127.0.0.1:6379/1"

    class Config:
        case_sensitive = True
        env_file = '.env', '.env.prod'
        env_file_encoding = 'utf-8'


def configure_logger():
    logger = logging.getLogger(__name__)
    return logger


settings = Settings()
logger = configure_logger()
