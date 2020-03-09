from abc import ABC
from abc import abstractmethod
from typing import List

from domain.model.register import Register


class RegisterReaderRepository(ABC):

    @abstractmethod
    def list_registers_by_users(
            self,
            user_1: str,
            user_2: str,
    ) -> List[Register]:
        pass
