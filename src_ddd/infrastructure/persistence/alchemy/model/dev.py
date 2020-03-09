from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func

from infrastructure.persistence.alchemy.model import Base


class Dev(Base):
    __tablename__ = "dev"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    registered_at = Column(DateTime, default=func.now(), nullable=False)

    def __init__(
            self,
            name: str,
    ):
        self.name = name
