from .DateExceptiond import *


class Date:
    """
        Class - Date
        
        Data members
        
        Year - integer
        Mounth - integer
        Day - integer
        Data methods
        
        Constructor - 3 params for init year, mounth, day
        
        __repr__ for print Date objet like - day.mount.year
        
        Ex. 15.10.1950
        add_day - add day to given Date object
        Add_mount - add mount to given Date object
        Add_year - add year to given Date object
        
        __is_leap_year - check year is leap or not
    """

    def __init__(self, year: int, mouth: int, day: int):
        self.__year = year
        self.__mount = self.check_mouth(mouth)
        self.__day = self.check_day(day)

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    @property
    def mount(self):
        return self.__mount

    @mount.setter
    def mount(self, value):
        self.__mount = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def day_in_mouth(self, m: int) -> int:
        mouthes = {
            1: 31,
            2: 29 if self.__is_leap_year() else 28,
            3: 30,
            4: 31,
            5: 30,
            6: 31,
            7: 30,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        return mouthes[m]

    def check_day(self, d):
        day_count = self.day_in_mouth(self.mount)
        if 0 <= d <= day_count:
            return d
        else:
            raise DayOutOfRangeError(d, day_count)

    def check_mouth(self, m):
        if 1 <= m <= 12:
            return m
        else:
            raise MouthOutOfRangeError(m)

    def __repr__(self) -> str:
        return "{}.{}.{}".format(self.day, self.mount, self.year)

    def add_day(self, d: int):
        if self.day + d > self.day_in_mouth(self.mount):
            delta = self.day + d
            while delta > self.day_in_mouth(self.mount):
                delta -= self.day_in_mouth(self.mount)
                self.add_mount(1)
            self.day = delta
        else:
            self.day += d

    def add_mount(self, m: int):
        if self.mount + m > 12:
            delta = self.mount + m
            k = delta // 12
            self.add_year(k)
            self.mount = delta - k * 12
        else:
            self.mount += m

    def add_year(self, year: int):
        self.year += year

    def __is_leap_year(self):
        if self.year % 4 == 0 and self.year % 100 == 0 and self.year % 400 == 0:
            return "The given year is a leap year"
        return "It is not a leap year"

