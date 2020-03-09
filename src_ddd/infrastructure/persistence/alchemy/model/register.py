from typing import List

from sqlalchemy import ARRAY
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func

from data.database import Base


class Register(Base):
    __tablename__ = "register"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    dev1_id = Column(Integer, ForeignKey("dev.id"))
    dev2_id = Column(Integer, ForeignKey("dev.id"))
    connected = Column(Boolean, nullable=False)
    organisations = Column(ARRAY(String))
    registered_at = Column(DateTime, default=func.now(), nullable=False)

    def __init__(
            self,
            dev1_id: int,
            dev2_id: int,
            connected: bool,
            organisations: List[str],
    ):
        self.dev1_id = dev1_id
        self.dev2_id = dev2_id
        self.connected = connected
        self.organisations = organisations
