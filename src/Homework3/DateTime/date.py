import datetimeError


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
        self._year = year
        self._mount = self.check_mouth(mouth)
        self._day = self.check_day(day)

    def day_in_mouth(self, m):
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
        day_count = self.day_in_mouth(self._mount)
        if 0 <= d <= day_count:
            return d
        else:
            raise datetimeError.DayOutOfRangeError(d, day_count)

    def check_mouth(self, m):
        if 1 <= m <= 12:
            return m
        else:
            raise datetimeError.MouthOutOfRangeError(m)

    def __repr__(self) -> str:
        return "{}.{}.{}".format(self._day, self._mount, self._year)

    def add_day(self, d: int):
        if self._day + d > self.day_in_mouth(self._mount):
            delta = self._day + d
            while delta > self.day_in_mouth(self._mount):
                delta -= self.day_in_mouth(self._mount)
                self.add_mount(1)
            self._day = delta
        else:
            self._day += d

    def add_mount(self, m: int):
        if self._mount + m > 12:
            delta = self._mount + m
            while delta > 12:
                delta -= 12
                self.add_year(1)
            self._mount = delta
        else:
            self._mount += m

    def add_year(self, year: int):
        self._year += year

    def __is_leap_year(self):
        if self._year % 4 == 0 and self._year % 100 == 0 and self._year % 400 == 0:
            return "The given year is a leap year"
        return "It is not a leap year"

