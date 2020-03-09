from datetime import datetime


class Dev:
    def __init__(
            self,
            id: int,
            name: str,
            registered_at: datetime,
    ):
        self.__id = id
        self.__name = name
        self.__registered_at = registered_at

    def id(self):
        return self.__id

    def name(self):
        return self.__name

    def registered_at(self):
        return self.__registered_at
