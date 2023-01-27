from myTime import Time
from myDate import Date


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

    def __init__(self, year: int, month: int, day: int, hour: int = 0, minute: int = 0, second: int = 0):
        self.__date = Date(year, month, day)
        self.__time = Time(hour, minute, second)

    def __repr__(self) -> str:
        return "{} {}".format(self.__date, self.__time)

    def __add__(self, other: "DateTime"):
        self.add_day(other.__date.day)
        self.add_month(other.__date.mount)
        self.add_year(other.__date.year)
        self.add_second(other.__time.second)
        self.add_minute(other.__time.minute)
        self.add_hour(other.__time.hour)

    def __sub__(self, other: "DateTime"):
        self.sub_day(other.__date.day)
        self.sub_month(other.__date.mount)
        self.sub_year(other.__date.year)
        self.sub_second(other.__time.second)
        self.sub_minute(other.__time.minute)
        self.sub_hour(other.__time.hour)

    def get_date(self):
        return self.__date

    def set_date(self, date: Date):
        self.__date = date

    def get_time(self):
        return self.__time

    def set_time(self, time: Time):
        self.__time = time

    def add_year(self, y: int):
        self.__date.year += y

    def sub_year(self, y: int):
        self.__date.year -= y

    def add_month(self, m: int):
        if self.__date.mount + m > 12:
            delta = self.__date.mount + m
            while delta > 12:
                delta -= 12
                self.add_year(1)
            self.__date.mount = delta
        else:
            self.__date.mount += m

    def sub_month(self, m: int):
        if self.__date.mount - m < 0:
            delta = m - self.__date.mount
            while delta > 12:
                delta -= 12
                self.sub_year(1)
            self.__date.mount = delta
        else:
            self.__date.mount -= m

    def add_day(self, d: int):
        if self.__date.day + d > self.__date.day_in_mouth(self.__date.mount):
            delta = self.__date.day + d
            while delta >= self.__date.day_in_mouth(self.__date.mount):
                print(delta)
                delta -= self.__date.day_in_mouth(self.__date.mount)
                self.add_month(1)
            print(delta)
            self.__date.day = delta
        else:
            self.__date.day += d

    def sub_day(self, d: int):
        if self.__date.day - d <= 0:
            delta = self.__date.day - d

            while delta < 0:
                c_days = self.__date.day_in_mouth(self.__date.mount)
                if delta > c_days:
                    delta += c_days
                    self.sub_month(1)
                else:
                    delta = c_days + delta
                    self.sub_month(1)

            self.__date.day = delta

        else:
            self.__date.day -= d

    def add_hour(self, h: int):
        if self.__time.hour + h > 23:
            delta = self.__time.hour + h
            k = delta // 24
            self.add_day(k)
            self.__time.hour = delta - k * 24
        else:
            self.__time.hour += h

    def sub_hour(self, h: int):
        if self.__time.hour - h < 0:
            delta = self.__time.hour - h
            while delta < 0:
                delta += 24
                self.sub_day(1)
            self.__time.hour = delta
        else:
            self.__time.hour -= h

    def add_minute(self, m: int):
        k = self.__time.minute + m
        if k > 60:
            h = k // 60
            self.add_hour(h)
            self.__time.minute = k - h * 60
        else:
            self.__time.minute += m

    def sub_minute(self, m: int):
        if self.__time.minute - m < 0:
            delta = m - self.__time.minute
            k = delta // 60
            self.sub_hour(k)
            self.__time.minute = delta - k * 60
        else:
            self.__time.minute -= m

    def add_second(self, s: int):
        k = self.__time.second + s
        if k > 60:
            m = k // 60
            self.add_minute(m)
            self.__time.second = k - m * 60
        else:
            self.__time.second += s

    def sub_second(self, s: int):
        if self.__time.second - s < 0:
            delta = s - self.__time.second
            k = delta // 60
            self.sub_minute(k)
            self.__time.second = delta - k * 60
        else:
            self.__time.second -= s


def test():
    dateTime = DateTime(1999, 6, 21, 13, 45, 1)
    print(dateTime)
    dateTime.add_day(31)
    print(dateTime)
    dateTime.sub_day(31)
    print(dateTime)



test()
