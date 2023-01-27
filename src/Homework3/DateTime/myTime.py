import datetimeError


class Time:
    """
        Class - Time
        
        Data members
        Hour - int
        Minute - int
        Second - int
        
        Data methods

        __init__ constructor
        __repr__
        1. add_second(s)
        2. add_minute(m)
        3. add_hour(h)
    """

    def __init__(self, hour: int, minute: int, second: int):
        self.__hour = self.check_hour(hour)
        self.__minute = self.check_minute(minute)
        self.__second = self.check_second(second)

    def __repr__(self) -> str:
        return "{}:{}:{}".format(self.__hour, self.__minute, self.__second)

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        self.__second = value

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        self.__minute = value

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        self.__hour = value

    def check_hour(self, h):
        if 0 <= h < 24:
            return h
        else:
            raise datetimeError.HourOutOfRangeError(h)

    def check_minute(self, m):
        if 0 <= m < 60:
            return m
        else:
            raise datetimeError.MinuteOutOfRangeError(m)

    def check_second(self, s):
        if 0 <= s < 60:
            return s
        else:
            raise datetimeError.SecondOutOfRangeError(s)

    def add_hour(self, h: int):
        if self.hour + h > 23:
            self.hour = self.hour + h - 24
        else:
            self.hour += h

    def add_minute(self, m: int):
        k = self.minute + m
        if k >= 60:
            h = k // 60
            self.add_hour(h)
            self.minute = k - h * 60
        else:
            self.minute += m

    def add_second(self, s: int):
        k = self.second + s
        if k >= 60:
            m = k // 60
            self.add_minute(m)
            self.second = k - m * 60
        else:
            self.second += s

    @staticmethod
    def sum(t1: "Time", t2: "Time"):
        """
            Function return t1+t2
        """
        t1.add_second(t2.second)
        t1.add_minute(t2.minute)
        t1.add_hour(t2.hour)

        return t1

    def add_time(self, t: "Time"):
        self.add_second(t.second)
        self.add_minute(t.minute)
        self.add_hour(t.hour)
