from abc import ABC
from abc import abstractmethod
from typing import Optional

from domain.model.dev import Dev


class DevReaderRepository(ABC):

    @abstractmethod
    def detail_dev_by_name(
            self,
            name: str,
    ) -> Optional[Dev]:
        pass
