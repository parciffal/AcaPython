from .date import Date
from .time import Time

class DateTime:

    def __init__(self, y: int = 0, m: int = 0 , d: int = 0, ) -> None:
        self.__date = Date(y,)
        self.__time = Time()
