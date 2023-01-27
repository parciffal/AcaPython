from ...DateTime.myDate import Date
from ...Sociaty.University.university import University
from ..Person.person import Person
from ..Job.job import Job
from .studentExceptions import IncorectCourseException
from typing import List

class Student(Person):

    def __init__(self, name: str, 
                 surname: str, 
                 gender: bool,
                 age: int, 
                 address: str, 
                 university: University,
                 faculty: str,
                 course: int,
                 started_at: Date,
                 friends: List["Person"] = ..., 
                 job: List[Job] = ...):
        super().__init__(name, surname, gender, age, address, friends, job)
        self.__university = university
        self.__faculty = faculty
        self.__course = self.check_course(course)
        self.__started_at = started_at
    
    def __repr__(self) -> str:
        return "Name: {}\nSurname: {}\nGender: {}\nAge: {}\n"+\
               "University: {}\nFaculty: {}\nCourse: {}\nStartred at: {}".\
               format(self.name, self.surename, self.gender, self.age,
                      self.university, self.faculty, self.course, self.started_at)

    def check_course(self, course):
        if 0 < course < 5:
            return course
        else:
            raise IncorectCourseException(course)

    @property
    def started_at(self):
        return self.started_at

    @started_at.setter
    def started_at(self, value: Date):
        self.__started_at = value

    @property
    def course(self):
        return self.course

    @course.setter
    def course(self, value: int):
        self.__course = value

    @property
    def faculty(self):
        return self.faculty

    @faculty.setter
    def faculty(self, value: str):
        self.__faculty = value

    @property
    def university(self):
        return self.university

    @university.setter
    def university(self, value: University):
        self.__university = value