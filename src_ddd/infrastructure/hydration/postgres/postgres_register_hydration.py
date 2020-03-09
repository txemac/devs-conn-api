from typing import Dict

from infrastructure.persistence.alchemy.model import Register


class PostgresRegisterHydration:

    @staticmethod
    def hydrate(
            register: Dict
    ) -> Register:
        return Register(
            id=register.get('id'),
            dev1_id=register.get('dev1_id'),
            dev2_id=register.get('dev2_id'),
            connected=register.get('connected'),
            organisations=register.get('organisations'),
            registered_at=register.get('registered_at'),
        )
