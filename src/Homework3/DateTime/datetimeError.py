"""
    Date Error's
"""

class DateError(Exception):
    def __init__(self, *args: object) :
        super().__init__(*args)

    def __repr__(self):
        return "Incorrect Date"

class DayOutOfRangeError(DateError):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __repr__(self):
        return super().__repr__()+"\nDay out of range 0 to 31: {}".format(self.__value)


class MouthOutOfRangeError(DateError):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __repr__(self):
        return super().__repr__() + "\nMouth out of range 0 to 12: {}".format(self.__value)

class YearOutOfRangeError(DateError):
    def __init__(self, value):
        super().__init__(value)
        self.__value = value

    def __repr__(self):
        return super().__repr__() + "\nYear out of range: {}".format(self.__value)


"""
    Time Error's
"""

class TimeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

    def __repr__(self) -> str:
        return "Incorrect Time"



