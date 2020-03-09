from typing import List

from sqlalchemy import and_
from sqlalchemy.orm import Session

from domain.model.repository.register_reader_repository import RegisterReaderRepository
from infrastructure.persistence.alchemy.model.dev import Dev
from infrastructure.persistence.alchemy.model.register import Register


class AlchemyRegisterReaderRepository(RegisterReaderRepository):

    def __init__(
            self,
            session: Session
    ):
        self._session = session

    def list_registers_by_users(
            self,
            dev1_id: int,
            dev2_id: int,
    ) -> List[Dev]:
        return self._session.query(Register) \
            .filter(and_(Register.dev1_id.in_([dev1_id, dev2_id]), Register.dev2_id.in_([dev1_id, dev2_id]))) \
            .all()
