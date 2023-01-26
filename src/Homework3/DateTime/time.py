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
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __repr__(self) -> str:
        return "{}:{}:{}".format(self.__hour, self.__minute, self.__second)

    def add_hour(self, h: int):
        if self.__hour + h > 24:
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
