from operator import and_
from typing import List

from sqlalchemy import ARRAY
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Session

from data.database import Base
from data.database.organisation import Organisation
from data.database.user import User
from data.schemas import RealtimeDB
from data.schemas import RealtimeGet
from data.schemas import RealtimePost


class Realtime(Base):
    __tablename__ = "realtime"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_1_id = Column(Integer, ForeignKey("user.id"))
    user_2_id = Column(Integer, ForeignKey("user.id"))
    connected = Column(Boolean, nullable=False)
    organisations = Column(ARRAY(String))
    registered_at = Column(DateTime, default=func.now(), nullable=False)

    def __init__(
            self,
            user_1_id: int,
            user_2_id: int,
            connected: bool,
            organisations: List,
    ):
        self.user_1_id = user_1_id
        self.user_2_id = user_2_id
        self.connected = connected
        self.organisations = organisations

    @classmethod
    def create(
            cls,
            db_session: Session,
            data: RealtimePost
    ):
        """
        Create a new real time.

        :param Session db_session: database session
        :param RealtimePost data: data
        """
        user_1 = User.get_or_create_by_name(db_session=db_session, name=data.user_1)
        user_2 = User.get_or_create_by_name(db_session=db_session, name=data.user_2)

        organisations_id = Organisation.get_ids_from_names(db_session=db_session, names=data.organisations) \
            if data.connected is True else None

        transaction = Realtime(
            user_1_id=user_1.id,
            user_2_id=user_2.id,
            connected=data.connected,
            organisations=organisations_id
        )
        db_session.add(transaction)
        db_session.commit()
        db_session.refresh(transaction)

    @classmethod
    def get_all_by_users(
            cls,
            db_session: Session,
            data: RealtimeGet
    ) -> List[RealtimeDB]:
        """

        :param Session db_session: database session
        :param RealtimeGet data: data
        :return Realtime: list realtime
        """
        """
        select * from realtime where user_1_id in (1, 2) and user_2_id in (1, 2);
        """
        user_1 = User.get_by_name(db_session=db_session, name=data.user_1)
        user_2 = User.get_by_name(db_session=db_session, name=data.user_2)

        return db_session.query(cls) \
            .filter(and_(cls.user_1_id.in_([user_1.id, user_2.id]), cls.user_2_id.in_([user_1.id, user_2.id]))) \
            .all() if None not in [user_1, user_2] else []
