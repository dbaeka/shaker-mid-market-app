from pathlib import Path
from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

from app.db.session import SessionLocal
from app.tests.utils.utils import get_user_token_headers
from main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def user_token_headers() -> Dict[str, str]:
    return get_user_token_headers()


@pytest.fixture(scope="module")
def resources():
    return Path(__file__).parent / "resources"
