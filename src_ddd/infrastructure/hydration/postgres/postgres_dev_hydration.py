from typing import Dict

from domain.model.dev import Dev


class PostgresDevHydration:

    @staticmethod
    def hydrate(
            dev: Dict
    ) -> Dev:
        return Dev(
            id=dev.get('id'),
            name=dev.get('name'),
            dt_created=dev.get('dt_created'),
        )
