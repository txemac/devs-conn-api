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
    user_1_id: int
    user_2_id: int


class RealtimePost(BaseModel):
    user_1: str
    user_2: str
    connected: bool
    organisations: List[str]


class RealtimeDB(RealtimePost):
    id: int
    registered_at: datetime
