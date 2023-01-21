from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.conversion import create_random_conversion


def test_create_successful_conversion(
        client: TestClient, user_token_headers: dict, db: Session
) -> None:
    data = {
        "amount": 10,
        "from_currency": "USD",
        "to_currency": "GHS"
    }
    response = client.post(
        f"{settings.API_V1_STR}/rates/convert", headers=user_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()

    assert content["rate"] > 0
    assert content["metadata"]
    assert content["converted_amount"] > 0
    assert content["metadata"]["from_currency"] == data["from_currency"]
    assert content["metadata"]["to_currency"] == data["to_currency"]


def test_create_wrong_request_conversion(
        client: TestClient, user_token_headers: dict, db: Session
) -> None:
    data = {
        "amount": 10,
        "from_currency": "USA",
        "to_currency": "GHS"
    }
    response = client.post(
        f"{settings.API_V1_STR}/rates/convert", headers=user_token_headers, json=data,
    )
    assert response.status_code == 400
    content = response.json()

    assert "Invalid from_currency" in content["detail"]


def test_get_history(
        client: TestClient, user_token_headers: dict, db: Session
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/rates/history", headers=user_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert len(content) > 0
    retrieved_conversion = content[-1]
    assert retrieved_conversion["converted_amount"] > 0
    assert retrieved_conversion["metadata"]


def test_get_currencies(
        client: TestClient, user_token_headers: dict, db: Session
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/rates/currencies", headers=user_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert len(content.items()) > 0
    assert content.get("Us Dollar")
    assert content.get("Us Dollar") == "USD"
