from typing import List

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import func
from sqlalchemy.orm import Session

from data.database import Base
from data.schemas import OrganisationDB
from data.schemas import OrganisationPost


class Organisation(Base):
    __tablename__ = "organisation"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
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
            data: OrganisationPost,
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

        return cls.get_by_name(db_session=db_session, name=data.name)

    @classmethod
    def get_or_create_by_name(
            cls,
            db_session: Session,
            name: str,
    ) -> OrganisationDB:
        """
        Get an organisation. Created if it does not exists.

        :param Session db_session: database session
        :param str name: name
        :return OrganisationDB: organisation
        """
        organisation = cls.get_by_name(db_session=db_session, name=name)
        if organisation is None:
            organisation = cls.create(db_session=db_session, data=OrganisationPost(name=name))
        return organisation

    @classmethod
    def get_by_name(
            cls,
            db_session: Session,
            name: str,
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

    @classmethod
    def get_ids_from_names(
            cls,
            db_session: Session,
            names: List[str],
    ) -> List[int]:
        """
        Get ids from a list of organisation names.

        :param Session db_session: database session
        :param list names: list of names
        :return list: ids
        """
        return [organisation.id for organisation in
                [Organisation.get_or_create_by_name(db_session=db_session, name=name)
                 for name in names]]

    @classmethod
    def get_names_from_ids(
            cls,
            db_session: Session,
            ids: List[str],
    ) -> List[int]:
        """
        Get names from a list of organisation ids.

        :param Session db_session: database session
        :param list ids: list of ids
        :return list: ids
        """
        return [organisation.name for organisation in
                [db_session.query(cls).get(organisation_id) for organisation_id in ids]]
