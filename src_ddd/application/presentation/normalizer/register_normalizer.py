from typing import Dict
from typing import Union

from domain.model.register import Register


class RegisterNormalizer:

    @staticmethod
    def normalize(
            register: Register
    ) -> Dict[str, Union[str, int]]:
        return dict(
            id=register.id(),
            dev1_id=register.dev1_id(),
            dev2_id=register.dev2_id(),
            connected=register.connected(),
            organizations=register.organizations(),
            registered_at=register.registered_at(),
        )
