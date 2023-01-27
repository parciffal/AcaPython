from Homework3.Sociaty.Person.person import Person


class City:

    def __init__(self, 
                 name: str, 
                 mayor: Person, 
                 population: int, 
                 language: str):
        self.__name = name
        self.__mayor = mayor
        self.__population = population
        self.__lenguage = language
    
    def __repr__(self) -> str:
        return "Name: {}\nPopulation: {}\nLenguage: {}\nMayor: \n{}"\
                .format(self.name, self.population, self.lenguage, self.mayor.__repr__())

    @property
    def lenguage(self):
        return self.__lenguage

    @lenguage.setter
    def lenguage(self, value: str):
        self.__lenguage = value

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value: int):
        self.__population = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def mayor(self):
        return self.__mayor
    
    @mayor.setter
    def mayor(self, value):
        self.__mayor = value

