from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Session

from data import Base
from data.schemas import UserDB
from data.schemas import UserPost


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    registered_at = Column(DateTime, default=func.now(), nullable=False)

    def __init__(
            self,
            name: str,
    ):
        self.name = name

    @classmethod
    def create(
            cls,
            db_session: Session,
            data: UserPost
    ) -> UserDB:
        """
        Create a new user.

        :param Session db_session: database session
        :param UserPost data: data
        :return UserDB: user
        """
        user = User(name=data.name)
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        return db_session.query(cls).filter(cls.name == data.name).first()

    @classmethod
    def get_or_create_by_name(
            cls,
            db_session: Session,
            name: str
    ) -> UserDB:
        """
        Get an user. Create if it does not exists.

        :param Session db_session: database session
        :param str name: name
        :return UserDB: user
        """
        user = db_session.query(cls).filter(cls.name == name).first()
        if user is None:
            user = cls.create(db_session=db_session, data=UserPost(name=name))
        return user
