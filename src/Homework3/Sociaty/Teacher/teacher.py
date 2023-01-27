from Homework3.DateTime.myDate import Date
from Homework3.Sociaty.University.university import University
from Homework3.money.money import Money
from ..Person.person import Person
from ..Job.job import Job
from typing import List

class Teacher(Person):
    
    def __init__(self, 
                 name: str, 
                 surname: str, 
                 gender: bool, 
                 age: int, 
                 address: str,
                 university: University,
                 facultet: str,
                 experience: int,
                 start_work_at: Date,
                 subject: str,
                 salary: Money,
                 friends: List["Person"] = ..., 
                 job: List[Job] = ...):
        super().__init__(name, surname, gender, age, address, friends, job)
        self.__university = university
        self.__facultet = facultet
        self.__experience = experience
        self.__start_work_at = start_work_at
        self.__subject = subject
        self.__salary = salary
    
    def __repr__(self) -> str:
        return "Name: {}\nSurname: {}\nGender: {}\nAge: {}\n"+\
               "University: {}\nFacultet: {}\nExperience: {}"+\
               "\nStart work at: {}\nSubject: {}\nSalary: {}".\
               format(self.name, self.surename, self.gender, self.age,
                      self.university.name, self.facultet, self.experience.__repr__(),
                      self.subject, self.salary.__repr__())

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value: Money):
        self.__salary = value

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, value: str):
        self.__subject = value

    @property
    def start_work_at(self):
        return self.__start_work_at

    @start_work_at.setter
    def start_work_at(self, value: Date):
        self.__start_work_at = value

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, value: int):
        self.__experience = value

    @property
    def facultet(self):
        return self.__facultet

    @facultet.setter
    def facultet(self, value: str):
        self.__facultet = value

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, value: University):
        self.__university = value
    
