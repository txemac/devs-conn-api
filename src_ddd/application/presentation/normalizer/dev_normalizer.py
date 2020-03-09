from typing import Dict
from typing import Union

from domain.model.dev import Dev


class UserNormalizer:

    @staticmethod
    def normalize(
            dev: Dev
    ) -> Dict[str, Union[str, int]]:
        return dict(
            id=dev.id(),
            name=dev.name(),
            registered_at=dev.registered_at(),
        )
