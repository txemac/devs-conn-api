from abc import ABC
from abc import abstractmethod
from typing import Optional

from domain.model.user import User


class UserReaderRepository(ABC):

    @abstractmethod
    def detail_user_by_name(
            self,
            name: str,
    ) -> Optional[User]:
        pass
