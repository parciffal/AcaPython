from ..Company.company import Company
from ...money.money import Money


class Job:
    
    def __init__(self, company: Company, salary: Money, 
                 experience_year: int, position: str):
        self.__company = company
        self.__salary = salary
        self.__experience_year = experience_year
        self.__position = position

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value: Company):
        self.__company = value
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: Money):
        self.__salary = value
    
    @property
    def experience_year(self):
        return self.__experience_year

    @experience_year.setter
    def experience_year(self, value):
        self.__experience_year = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value: str):
        self.__position = value

    def __repr__(self) -> str:
        return "Company: {}\n"\
               "Salary: {}\n"\
               "Experience Year: {}\n"\
               "Position: {}\n".\
               format(self.company, 
                      self.salary, 
                      self.experience_year, 
                      self.position)
    
    def change_salary(self, value: Money):
        self.salary = value

    def change_experience_year(self, value):
        self.experience_year = value

    def change_postition(self, value: str):
        self.position = value


