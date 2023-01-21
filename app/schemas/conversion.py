from datetime import datetime

from pydantic import BaseModel, Field, validator


def amount_round(v):
    return round(v, 2)


def capitalize(v):
    return v.upper()


# properties to receive for creation
class ConversionCreate(BaseModel):
    amount: float = Field(gt=0, description="Amount to convert. Should be greater than 0")
    from_currency: str = Field(min_length=3, max_length=3, description="ISO currency code of base currency")
    to_currency: str = Field(min_length=3, max_length=3, description="ISO currency code of destination currency")

    _round_amount = validator('amount', allow_reuse=True)(amount_round)
    _capitalize_currency = validator('from_currency', 'to_currency', allow_reuse=True)(capitalize)


class MetaData(BaseModel):
    time_of_conversion: datetime
    from_currency: str = Field(min_length=3, max_length=3, description="ISO currency code of base currency")
    to_currency: str = Field(min_length=3, max_length=3, description="ISO currency code of destination currency")


class Conversion(BaseModel):
    converted_amount: float
    rate: float
    metadata: MetaData

    _round_amount = validator('converted_amount', allow_reuse=True)(amount_round)

    @validator('rate')
    def rate_round(cls, v):
        return round(v, 5)


class ConversionInDBCreate(BaseModel):
    value: Conversion


# Properties stored in DB
class ConversionInDB(BaseModel):
    id: int
    value: Conversion
    owner_id: int
    created_at: datetime | None = None

    class Config:
        orm_mode = True
