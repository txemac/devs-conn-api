from typing import Optional

from sqlalchemy.orm import Session

from domain.model.repository.dev_reader_repository import DevReaderRepository
from infrastructure.persistence.alchemy.model.dev import Dev


class AlchemyDevReaderRepository(DevReaderRepository):

    def __init__(
            self,
            session: Session
    ):
        self._session = session

    def detail_dev_by_name(
            self,
            name: str,
    ) -> Optional[Dev]:
        return self._session.query(Dev).filter_by(name=name).first()
