from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, models, crud
from app.api.dependencies import get_current_user, get_db
from app.core.config import logger
from app.exceptions.internal import WrongCurrencyCodeException
from app.services.currencies import CurrenciesService
from app.services.rates import RatesService

router = APIRouter()


@router.get("/currencies", response_model=dict[str, str])
async def read_currencies(current_user: models.User = Depends(get_current_user)) -> dict[str, str]:
    """
    Get list of currencies supported by the rate provider.
    """
    logger.info("Getting list of currencies")
    svc = CurrenciesService()
    currencies = await svc.get_list()
    if currencies is None:
        logger.error("Trouble getting currencies. Provider might be down")
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="Could not get currencies")
    return currencies


@router.get("/history", response_model=list[schemas.Conversion])
def read_items(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(get_current_user),
) -> Any:
    """
    Retrieve historic conversions made.
    """
    logger.info("Getting historic conversions")
    conversions = crud.conversion.get_multi_by_owner(db=db, owner_id=current_user.id, skip=skip, limit=limit)

    return [conversion.value for conversion in conversions]


@router.post("/convert", response_model=schemas.Conversion)
async def create_conversion(
        *,
        db: Session = Depends(get_db),
        conversion_in: schemas.ConversionCreate,
        current_user: models.User = Depends(get_current_user),
) -> Any:
    """
    Create new conversion based on mid-rate.
    """
    logger.info("Converting currencies using rate")
    svc = RatesService()
    try:
        result = await svc.convert(conversion_in)
    except WrongCurrencyCodeException as e:
        logger.info("Wrong Currency provided as input")
        raise HTTPException(status_code=400, detail=str(e))
    crud.conversion.create_with_owner(db=db, obj_in={"value": result}, owner_id=current_user.id)
    return result
