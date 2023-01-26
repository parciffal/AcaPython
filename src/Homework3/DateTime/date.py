from .datetimeError import DateError, DayOutOfRangeError, MouthOutOfRangeError, YearOutOfRangeError

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
        if 0 <= d <= self.day_in_mouth(self.__mount):
            return d
        else:
            raise DayOutOfRangeError(d)
    
    def check_mouth(self, m):
        if 1<= m <= 12:
            return m
        else:
            raise MouthOutOfRangeError(m)
    

    def __repr__(self) -> str:
        return "{}.{}.{}".format(self.__day, self.__mount, self.__year)

    def add_day(self, d: int):
        current_m_days = self.day_in_mouth(self.__mount)
        if self.
        self.__day = d

    def add_mount(self, m: int):
        if self.__mount + m >= 12:
            self.__year += 1 
            self.__mount = 1 if self.__mount + m == 12 else self.__mount + m - 12
        else:
            self.__mount += m

    def add_year(self, year: int):
        self.__year = year

    def __is_leap_year(self):
        if self.__year % 4 == 0 and self.__year % 100 == 0 and self.__year % 400 == 0:
            return "The given year is a leap year"
        return "It is not a leap year"


class DateError(Exception):
    def __init__(self):
        pass
