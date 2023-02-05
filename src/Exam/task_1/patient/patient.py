from typing import List


class AgeOutOfRange(Exception):
    def __init__(self, age: int) -> None:
        super().__init__("Age out range 18 .. 100 : {}".format(age))


class Patient:
    def __init__(self, name: str, 
                       surname: str, 
                       gender: bool, 
                       age: int):
        self.__name = name
        self.__surname = surname
        self.__gender = 'M' if gender else 'F'
        self.__age = self.check_age(age)

    def check_age(self, age):
        if 18 <= age <= 100:
            return age
        else:
            raise AgeOutOfRange(age)
    
    def __repr__(self) -> str:
        return "\n {} {} - {}, {} years old".\
               format(self.name, self.surname, self.gender, self.age)
    
    def __ne__(self, __o: "Patient") -> bool:
        if self.name == __o.name and self.surname == __o.surname:
            if self.age == __o.age and self.gender == __o.gender:
                return False
            else:
                return True
        else:
            return True

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        self.__age = self.check_age(value)

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value: bool):
        self.__gender = 'M' if value else 'F'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value: str):
        self.__surname = value

    