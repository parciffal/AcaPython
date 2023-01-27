from typing import List

from ...money.money import Money
from ..Person.person import Person
from ..Job.job import Job


class Doctor(Person):

    def __init__(self,
                 name: str,
                 surname: str, 
                 gender: bool,
                 age: int, 
                 address: str, 
                 department: str,
                 profession: str,
                 patronymic: str,
                 salary: Money,
                 friends: List[Person] = [], 
                 job: List[Job] = [],):
        super().__init__(name, surname, gender, age, address, friends, job)
        self.__department = department
        self.__profession = profession
        self.__patronymic = patronymic
        self.__salary = salary

    def __repr__(self) -> str:
        return "Name: {}\nSurname: {}\nGender: {}\nAge: {}\n"+\
               "Profession: {}\nDepartment: {}\n Patronymic: {}\n Salary: {}\n"\
               .format(self.name, self.surename, self.gender, self.age, self.profession, 
                       self.department, self.patronymic, self.salary.__repr__())
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: Money):
        self.__salary = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value: str):
        self.__patronymic = value
    
    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value: str):
        self.__department = value

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, value:str):
        self.__profession = value

    

