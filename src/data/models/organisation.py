from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Session

from data import Base
from data.schemas import OrganisationDB
from data.schemas import OrganisationPost


class Organisation(Base):
    __tablename__ = "organisation"

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
            data: OrganisationPost
    ) -> OrganisationDB:
        """
        Create a new organisation.

        :param Session db_session: database session
        :param OrganisationPost data: data
        :return OrganisationDB: organisation
        """
        user = Organisation(name=data.name)
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        return db_session.query(cls).filter(cls.name == data.name).first()

    @classmethod
    def get_or_create_by_name(
            cls,
            db_session: Session,
            name: str
    ) -> OrganisationDB:
        """
        Get an organisation. Created if it does not exists.

        :param Session db_session: database session
        :param str name: name
        :return OrganisationDB: organisation
        """
        organisation = db_session.query(cls).filter(cls.name == name).first()
        if organisation is None:
            organisation = cls.create(db_session=db_session, data=OrganisationPost(name=name))
        return organisation
