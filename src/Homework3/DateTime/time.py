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
        self._hour = self.check_hour(hour)
        self._minute = self.check_minute(minute)
        self._second = self.check_second(second)

    def __repr__(self) -> str:
        return "{}:{}:{}".format(self.__hour, self.__minute, self.__second)
    
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
        if self.__hour + h > 23:
            self.__hour = self.__hour + h - 24
        else:
            self.__hour += h

    def add_minute(self, m: int):
        k = self.__minute + m
        if k >= 60:
            h = k // 60
            self.add_hour(h)
            self.__minute = k - h * 60
        else:
            self.__minute += m

    def add_second(self, s: int):
        k = self.__second + s
        if k >= 60:
            m = k // 60
            self.add_minute(m)
            self.__second = k - m * 60
        else:
            self.__second += s

    @staticmethod
    def sum(t1: "Time", t2: "Time"):
        """
            Function return t1+t2
        """
        t1.add_second(t2.__second)
        t1.add_minute(t2.__minute)
        t1.add_hour(t2.__hour)

        return t1

    def add_time(self, t: "Time"):
        self.add_second(t.__second)
        self.add_minute(t.__minute)
        self.add_hour(t.__hour)

