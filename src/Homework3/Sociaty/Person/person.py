from typing import List
from ..Job.job import Job
from .personExceptions import AgeOutOfRange


class Person:
    
    def __init__(self, name: str, surname: str,
                 gender: bool, age: int, address: str,
                 friends: List["Person"] = ...,job: List[Job] = ...): 
        self.__name = name
        self.__surename = surname
        self.__gender = 'Male' if gender else 'Female'
        self.__age = self.check_age(age)
        self.__address = address
        self.__friends = friends
        self.__job = job
    
    def check_age(self, age):
        if 0 <= age <= 150:
            return age
        else:
            raise AgeOutOfRange(age)

    def __repr__(self) -> str:
        return "Name: {}\n"\
               "Surname: {}\n"\
               "Gender: {}\n"\
               "Age: {}\n"\
               "Address: {}\n"\
               "Friends: {}\n"\
               "Job: {}\n"\
               .format(
                       self.name,
                       self.surename,
                       self.gender,
                       self.age,
                       self.address,
                       [i.name for i in self.friends],
                       [i.position for i in self.job]
                       )

    def add_friend(self, value: "Person"):
        if value not in self.friends:
            self.friends.append(value)

    def remove_friend(self, value: "Person"):
        self.friends.remove(value)

    def add_job(self, value: Job):
        if value not in self.job:
            self.job.append(value)
            for i in self.job:
                if i == value:
                    i.company.add_employee()
    
    def remove_job(self, value: Job):
        self.job.remove(value)
        for i in self.job:
            if i == value:
                i.company.del_employee()

    def display_job(self):
        [print(i) for i in self.job]

    def display_friens(self):
        [print(i) for i in self.friends]


    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, value: List[Job]):
        self.__job = value

    @property
    def friends(self):
        return self.__friends

    @friends.setter
    def friends(self, value: List['Person']):
        self.__friends = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        self.__address = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        self.__age = value
    
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value: bool):
        self.__gender = 'Male' if value else 'Female'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value
    
    @property
    def surename(self):
        return self.__surename

    @surename.setter
    def surename(self, value: str):
        self.__surename = value
    

 
