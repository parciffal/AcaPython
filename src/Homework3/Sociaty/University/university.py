from ..Person.person import Person
from ..City.city import City
from ...DateTime.myDate import Date

class University:
    """
    Class University
    Data members:
    1. name: string
    2. founded_at: Date class
    3. rector: Pereson class
    4. city: City class
    Data methods:
    1. __init__
    2. __repr__
    3. get_name (name=name)
    4. set_name (name=name)
    5. get_founded_at (name=founded_at)
    6. set_rector (name=rector)
    7. get_rector (name=rector)
    8. get_city (name=city)
    """
    
    def __init__(self, name: str, founded_at: Date, rector: Person, city: City):
        self.__name = name
        self.__founded_at = founded_at
        self.__rector = rector
        self.__city = city

    def __repr__(self) -> str:
        return "Name: {}\nFounded at: {}\nRector: {}\n City: {}"\
               .format(self.name, self.founded_at, self.rector.name, self.city.name)

    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self, value: City):
        self.__city = value

    @property
    def rector(self):
        return self.__rector
    
    @rector.setter
    def rector(self, value: Person):
        self.__rector = value

    @property
    def founded_at(self):
        return self.__founded_at
    
    @founded_at.setter
    def founded_at(self, value: Date):
        self.__founded_at = value

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value: str):
        self.__name = value

    

