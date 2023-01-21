from pydantic import BaseModel


# shared properties
class StoredData(BaseModel):
    timestamp: int
    data: dict[str, str]
    provider_timestamp: int | None = None
