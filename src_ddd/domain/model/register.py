from datetime import datetime
from typing import List


class Register:
    def __init__(
            self,
            id: int,
            user_1_id: int,
            user_2_id: int,
            connected: bool,
            organizations: List[str],
            registered_at: datetime,
    ):
        self.__id = id
        self.__user_1_id = user_1_id
        self.__user_2_id = user_2_id
        self.__connected = connected
        self.__organizations = organizations
        self.__registered_at = registered_at

    def id(self):
        return self.__id

    def user_1_id(self):
        return self.__user_1_id

    def user_2_id(self):
        return self.__user_2_id

    def connected(self):
        return self.__connected

    def organizations(self):
        return self.__organizations
