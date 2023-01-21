from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.core.config import logger
from app.crud.base import CRUDBase
from app.models.conversion import Conversion
from app.schemas.conversion import ConversionInDB, ConversionInDBCreate


class CRUDConversion(CRUDBase[Conversion, ConversionInDBCreate]):
    def create_with_owner(
            self, db: Session, *, obj_in: ConversionInDBCreate, owner_id: int
    ) -> ConversionInDB:
        logger.info("Creating Conversion in DB instance for User: " + str(owner_id))
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
            self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[ConversionInDB]:
        return (
            db.query(self.model)
            .filter(Conversion.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


conversion = CRUDConversion(Conversion)
