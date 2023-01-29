"""
    Date Error's
"""


class DateError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)

    def __str__(self):
        return "Incorrect Date"


class DayOutOfRangeError(DateError):
    def __init__(self, value, dayCount):
        super().__init__(value)
        self.__value = value
        self.__dayCount = dayCount

    def __str__(self):
        return super().__str__() + "\nDay out of range 0 to {}: {}".format(self.__dayCount, self.__value)


class MouthOutOfRangeError(DateError):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __str__(self):
        return super().__str__() + "\nMouth out of range 0 to 12: {}".format(self.__value)


class YearOutOfRangeError(DateError):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __str__(self):
        return super().__str__() + "\nYear out of range: {}".format(self.__value)


"""
    Time Error's
"""


class TimeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __str__(self) -> str:
        return "Incorrect Time"


class HourOutOfRangeError(DateError):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __str__(self):
        return super().__str__() + "\nHour out of range 0 to 23: {}".format(self.__value)


class MinuteOutOfRangeError(DateError):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __str__(self):
        return super().__str__() + "\nMinute out of range 0 to 59: {}".format(self.__value)


class SecondOutOfRangeError(DateError):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __str__(self):
        return super().__str__() + "\nSecond out of range 0 to 59: {}".format(self.__value)
