from .date import Date
from .time import Time


class DateTime:
    """
        Class DateTime
        Data members:
        1. date: Date class
        2. time: Time class
        Data methods:
        1. __init__
        2. __repr__
        3. get_date (name=date)
        4. set_date (name=date)
        5. get_time (name=time)
        6. set_time (name=time)
        7. add_year
        8. add_month
        9. add_day
        10. add_hour
        11. add_minute
        12. add_second
        13. sub_year
        14. sub_month
        15. sub_day

        16. sub_hour
        17. sub_minute
        18. sub_second
        19. __add__
        20. __sub__

    """

    def __init__(self, y: int, m: int, d: int,
                 hour: int = 0, minute: int = 0, second: int = 0):
        self.__date = Date(y, m, d)
        self.__time = Time(hour, minute, second)

    def __repr__(self) -> str:
        return "{}-{}-{} {}:{}:{}".format(self.__date.__)
