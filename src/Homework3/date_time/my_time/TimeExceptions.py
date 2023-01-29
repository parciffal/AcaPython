class TimeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Incorrect Time"


class HourOutOfRangeError(Exception):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __str__(self):
        return super().__str__() + "\nHour out of range 0 to 23: {}".format(self.__value)


class MinuteOutOfRangeError(Exception):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __str__(self):
        return super().__str__() + "\nMinute out of range 0 to 59: {}".format(self.__value)


class SecondOutOfRangeError(Exception):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __str__(self):
        return super().__str__() + "\nSecond out of range 0 to 59: {}".format(self.__value)
