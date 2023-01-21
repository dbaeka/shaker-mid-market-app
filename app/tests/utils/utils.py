import base64
import random
import string

from app.core.config import settings


def random_float(places=2) -> float:
    return round(random.uniform(1.00, 1000.00), places)


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=32))


def get_user_token_headers() -> dict[str, str]:
    username = settings.TEST_USER
    password = settings.TEST_USER_PASSWORD
    key = f"{username}:{password}"
    key_bytes = key.encode("utf8")
    token = base64.b64encode(key_bytes).decode("utf8")
    headers = {"Authorization": f"Basic {token}"}
    return headers
