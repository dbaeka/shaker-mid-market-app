from datetime import datetime

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.conversion import Conversion, MetaData
from app.tests.utils.conversion import create_random_conversion
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string, random_float


def test_create_conversion(db: Session) -> None:
    user = create_random_user(db)
    amount = random_float(3)
    rate = random_float(5)
    from_currency = random_lower_string()[:3]
    to_currency = random_lower_string()[:3]
    metadata = MetaData(time_of_conversion=datetime.now(), from_currency=from_currency, to_currency=to_currency)
    conversion_in = Conversion(converted_amount=amount, rate=rate, metadata=metadata)
    conversion = crud.conversion.create_with_owner(db=db, obj_in={"value": conversion_in}, owner_id=user.id)
    assert jsonable_encoder(conversion.value) == jsonable_encoder(conversion_in)
    assert conversion.owner_id == user.id


def test_get_single_conversion(db: Session) -> None:
    conversion = create_random_conversion(db)
    stored_conversion = crud.conversion.get(db=db, id=conversion.id)
    assert stored_conversion
    assert conversion.id == stored_conversion.id
    assert jsonable_encoder(conversion) == jsonable_encoder(stored_conversion)


def test_get_multiple_conversions_by_owner(db: Session) -> None:
    user = create_random_user(db)
    create_random_conversion(db, owner_id=user.id)
    create_random_conversion(db, owner_id=user.id)
    stored_conversions = crud.conversion.get_multi_by_owner(db=db, owner_id=user.id)
    assert stored_conversions
    assert len(stored_conversions) == 2
    assert isinstance(stored_conversions[-1], models.Conversion)
