from datetime import datetime

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.conversion import Conversion, MetaData
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string, random_float


def create_random_conversion(db: Session, *, owner_id: int | None = None) -> models.Conversion:
    if owner_id is None:
        user = create_random_user(db)
        owner_id = user.id
    amount = random_float()
    rate = random_float(4)
    from_currency = random_lower_string()[:3]
    to_currency = random_lower_string()[:3]
    metadata = MetaData(time_of_conversion=datetime.now(), from_currency=from_currency, to_currency=to_currency)
    conversion_in = Conversion(converted_amount=amount, rate=rate, metadata=metadata)
    return crud.conversion.create_with_owner(db=db, obj_in={"value": conversion_in}, owner_id=owner_id)
