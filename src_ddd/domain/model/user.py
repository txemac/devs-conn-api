class User:
    def __init__(
            self,
            id: int,
            name: str,
    ):
        self.__id = id
        self.__name = name

    def id(self):
        return self.__id

    def name(self):
        return self.__name
