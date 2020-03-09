from abc import ABC
from abc import abstractmethod
from typing import List

from domain.model.register import Register


class RegisterReaderRepository(ABC):

    @abstractmethod
    def list_registers_by_users(
            self,
            dev1: int,
            dev2: int,
    ) -> List[Register]:
        pass
