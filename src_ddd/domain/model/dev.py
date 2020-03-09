from datetime import datetime


class Dev:
    def __init__(
            self,
            id: int,
            name: str,
            dt_created: datetime,
    ):
        self.__id = id
        self.__name = name
        self.__dt_created = dt_created

    def id(self):
        return self.__id

    def name(self):
        return self.__name
