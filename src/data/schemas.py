from datetime import datetime
from typing import List

from pydantic import BaseModel
from pydantic import Field


class OrganisationPost(BaseModel):
    name: str = Field(..., min_length=1, max_length=150)


class OrganisationDB(OrganisationPost):
    id: int
    registered_at: datetime


class UserPost(BaseModel):
    name: str = Field(..., min_length=1, max_length=150)


class UserDB(UserPost):
    id: int
    registered_at: datetime


class RealtimeGet(BaseModel):
    user_1: str = Field(..., min_length=1, max_length=150)
    user_2: str = Field(..., min_length=1, max_length=150)


class RealtimePost(BaseModel):
    user_1: str = Field(..., min_length=1, max_length=150)
    user_2: str = Field(..., min_length=1, max_length=150)
    connected: bool
    organisations: List[str] = None


class RealtimeDB(RealtimePost):
    id: int
    registered_at: datetime


class RealtimeOut(BaseModel):
    registered_at: datetime
    connected: bool
    organisations: List[str] = None
