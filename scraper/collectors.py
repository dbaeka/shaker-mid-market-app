import json
from typing import Any

import httpx

from app.core.config import logger


def get_data(url: str, headers: dict) -> Any:
    try:
        client = httpx.Client(timeout=httpx.Timeout(20.0), )
        response = client.get(url, headers=headers)

        if response.status_code == 200:
            body = json.loads(response.content)
            return body
    except Exception as e:
        logger.error("Error encountered collecting data: " + str(e))
