from datetime import datetime
from typing import List


class Register:
    def __init__(
            self,
            id: int,
            dev_1_id: int,
            dev_2_id: int,
            connected: bool,
            organizations: List[str],
            registered_at: datetime,
    ):
        self.__id = id
        self.__dev_1_id = dev_1_id
        self.__dev_2_id = dev_2_id
        self.__connected = connected
        self.__organizations = organizations
        self.__registered_at = registered_at

    def id(self):
        return self.__id

    def dev_1_id(self):
        return self.__dev_1_id

    def dev_2_id(self):
        return self.__dev_2_id

    def connected(self):
        return self.__connected

    def organizations(self):
        return self.__organizations

    def registered_at(self):
        return self.__registered_at
