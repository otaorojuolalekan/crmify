from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime as dt


class AccountBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    address: Optional[str]
    email: Optional[EmailStr]
    created_at: dt


class AccountCreate(BaseModel):
    first_name: str
    last_name: str
    address: Optional[str] = None
    email: Optional[EmailStr] = None


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserBase(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: dt


class UserOutput(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: dt

    class Config:
        form_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int]
    username: Optional[str]

class UpdateBase(BaseModel):
    update_text: str


class UpdateOutput(BaseModel):
    id: int
    created_at: dt
    update_text: str
    user_id: int
    update_created_by: UserBase
    case_id: int

    class Config:
        form_attributes = True


# create output for all and


class CaseBase(BaseModel):
    id: int
    category: str
    subject: str
    status: str
    created_at: dt
    user_id: int
    user: UserBase
    account_id: int
    account: AccountBase
    # updates: UpdateOutput


""" class CaseOutput(CaseBase):
    user: UserOutput
    account: AccountBase

    class Config():
        form_attributes = True """


class CaseCreate(BaseModel):
    category: str
    subject: str
    status: Optional[str] = "Unresolved"
    # account_id: int


class CasePatch(BaseModel):
    status: Optional[str] = "Resolved"


