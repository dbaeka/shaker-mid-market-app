from pydantic import BaseModel


# shared properties
class UserBase(BaseModel):
    username: str | None = None
    full_name: str | None = None


# properties from API to create user
class UserCreate(UserBase):
    username: str
    password: str


class UserInDBBase(UserBase):
    id: int | None = None

    class Config:
        orm_mode = True


# additional properties to return via API
class User(UserInDBBase):
    pass


# additional properties to stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
