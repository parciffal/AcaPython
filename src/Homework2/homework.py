"""
Task 1
Write a Python program to create a new dictionary by extracting the mentioned keys
from the below dictionary.
Example

sample_dict = {
'name': 'Kelly',
'age': 25,
'salary': 8000,
'city': 'New york'}
# Keys to extract
keys = ['name', 'salary']

# Expected output
{"name": "Kelly", "salary": 8000}

"""
def task_1(dct: dict, keys: list) -> dict:
    return {x:dct[x] for x in keys}

"""
Task 2
Get the key of a minimum value from the following dictionary.
Example:

sample_dict = {
'Physics': 82,
'Math': 65,
'history': 75
}

# Expected output
Math
"""
def task_2(dct: dict):
    return sorted(dct)[0]

#print(task_2(sample_dict))

"""
Task 3
Write a Python program to copy the contents of a file to another file
"""
def task_3(filename):
    with open(filename, 'r') as f:
        with open("1"+filename, 'w') as fs:
            fs.writelines(f.readlines())
#task_3('test.txt')
"""
Task 4
Write a Python program to count the frequency of words in a file
"""
def task_4(filename):
    with open(filename, 'r') as f:
        words = {}
        lines = f.readlines()
        for line in lines:
            line = line.strip().replace(',', ' ').replace('.', ' ')
            line = line.lower().split(" ")
            for i in line:
                if i in words:
                    words[i] += 1
                else:
                    words[i] = 1
    return words

"""
Task 5
Write a Python program to read last n lines of a file
"""
def task_5(filename, n):
    with open(filename, 'r') as f:
        return f.readlines()[n:-1]

"""
Task 6
Finish class work, which you started in class.
Class
Write class Company
Data members: company_name, founded_at, employees_count
Data methods: __init__, __repr__

Write class Job.
Data members: company(Company type), salary, experience_year, position.
Data methods: __init__, __repr__, change_salary, change_experience_year,
change_postition.
Write class Person.
Data members: name, surname, gender(Male or Female), age, address, friends(list
of Person type), job(list of Job type)
Data methods: __init__, __repr__, add_friend, remove_friend, add_job,
remove_job, display_job
Some logics
When Person add job Company employees count should increase by 1.
When Person quit the job Company employees count should decrease by 1.
You can come up with other logics.
"""
class Company():
    """
    Write class Company
    Data members: company_name, founded_at, employees_count
    Data methods: __init__, __repr__
    """

    def __init__(self, company_name, founded_at, employees_count):
        self.company_name = company_name
        self.founded_at = founded_at
        self.employees_count = employees_count
    
    def __repr__(self) -> str:    
        return "Name: {}\n"\
               "Founded at: {}\n"\
               "Employees Count: {}"\
               .format(self.company_name, 
                       self.founded_at, 
                       self.employees_count)
    
    def add_employee(self):
        self.employees_count += 1

    def del_employee(self):
        self.employees_count -= 1

class Job():
    """
    Write class Job.
    Data members: company(Company type), salary, experience_year, position.
    Data methods: __init__, __repr__, change_salary, change_experience_year,
    change_postition.
    """
    
    def __init__(self, company: Company, salary, experience_year, position):
        self.company = company
        self.__salary = salary
        self.__experience_year = experience_year
        self.__position = position

    def __repr__(self) -> str:
        return "Company: {}\n"\
               "Salary: {}\n"\
               "Experience Year: {}\n"\
               "Position: {}\n".\
               format(self.company, 
                      self.__salary, 
                      self.__experience_year, 
                      self.__position)
    
    def change_salary(self, value):
        self.__salary = value

    def change_experience_year(self, value):
        self.__experience_year = value

    def change_postition(self, value):
        self.__position = value


class Person():
    """
    Write class Person.

    Data members: name, surname, gender(Male or Female),
                  age, address, friends(list of Person type), 
                  job(list of Job type)

    Data methods: __init__, __repr__, add_friend, remove_friend,
                  add_job, remove_job, display_job
    """
    
    def __init__(self, name: str, surname: str,
                 gender: bool, age: int, address: str,
                 friends: list = [],job: list[Job] = []): 
        self.__name = name
        self.__surname = surname
        self.__gender = 'Male' if gender else 'Female'
        self.__age = age
        self.__address = address
        self.__friends = friends
        self.__job = job

    def __repr__(self) -> str:
        return "Name: {}\n"\
               "Surname: {}\n"\
               "Gender: {}\n"\
               "Age: {}\n"\
               "Address: {}\n"\
               "Friends: {}\n"\
               "Job: {}\n"\
               .format(
                       self.__name,
                       self.__surname,
                       self.__gender,
                       self.__age,
                       self.__address,
                       [i.__name for i in self.__friends],
                       [i._Job__position for i in self.__job]
                       )

    def add_friend(self, value: "Person"):
        if value not in self.__friends:
            self.__friends.append(value)

    def remove_friend(self, value: "Person"):
        self.__friends.remove(value)

    def add_job(self, value: Job):
        """
        When Person add job Company employees count should increase by 1.
        """
        if value not in self.__job:
            self.__job.append(value)
            for i in self.__job:
                if i == value:
                    i.company.add_employee()
    
    def remove_job(self, value: Job):
        self.__job.remove(value)
        for i in self.__job:
            if i == value:
                i.company.del_employee()

    def display_job(self):
        [print(i) for i in self.__job]

    def display_friens(self):
        [print(i) for i in self.__friends]
        
        
"""
google = Company("Google", "12.2.1998", 0)
job = Job(google, 100000, 4, "Developer")
job1 = Job(google, 200000, 3, "Lector")
edgar = Person("Edgar", "Khachikyan", True, 23, "Armenia")
edgar.add_job(job)
edgar.add_job(job1)
vardan = Person("Vardan", "Khachikyan", True, 21, "Armenia")
#edgar.remove_job(job)
edgar.add_friend(vardan)
print(edgar)
"""

"""
Task 7
Write this classes.
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

Class - Time
Data members
Hour - int
Minute - int
Second - int
Data methods

__init__ constructor
__repr__
3. add_second(s)
2. add_minute(m)
1.add_hour(h)
sum() - Գումարել երկու Time տիպի օբյեկտ(հաշվի առնել, որ վայրկյանները
գումարելուց կարող է փոխվել նաև րոպեն, րոպեները փոխվելուց նաև ժամը)
sum 2 Time objects (take into account that, when add seconds, minutes can be
changed, when add minutes hour can be changed, when add hours, can get value &gt;
24, that case should take hour%24 as hour)
Time() and Date() classes are very similar, but Time() is easy, because, in
Date() we have month with different days, but Time() all are standard, 1min =
60sec, 1hour = 60minute=3600second
"""

class Date():
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
    

    def __init__(self, year: int, mount: int, day: int):
        self.__year = year
        self.__mount = mount
        self.__day = day if day <= self.gen_mouthes(mount) else self.gen_mouthes(mount)      
    
    def gen_mouthes(self, m):
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


    def __repr__(self) -> str:
        return "{}.{}.{}".format(self.__day, self.__mount, self.__year)

    def add_day(self, d: int):

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
        

class Time():
    """
        Class - Time
        
        Data members
        Hour - int
        Minute - int
        Second - int
        
        Data methods

        __init__ constructor
        __repr__
        1. add_second(s)
        2. add_minute(m)
        3. add_hour(h)
    """

    def __init__(self, hour: int, minute: int, second: int):
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    
    def __repr__(self) -> str:
        return "{}:{}:{}".format(self.__hour, self.__minute, self.__second)

    def add_hour(self, h: int):
        if self.__hour + h > 24:
            self.__hour = self.__hour + h - 24
        else:
            self.__hour += h
    
    def add_minute(self, m: int):
        k = self.__minute + m
        if k >= 60: 
            h = k // 60
            self.add_hour(h)
            self.__minute = k - h*60
        else:
            self.__minute += m

    def add_second(self, s: int):
        k = self.__second + s
        if k >= 60:
            m = k // 60 
            self.add_minute(m)
            self.__second = k - m*60
        else:
            self.__second += s


    @staticmethod
    def sum(t1: "Time", t2: "Time"):
        """
            Function return t1+t2
        """
        t1.add_second(t2.__second)
        t1.add_minute(t2.__minute)
        t1.add_hour(t2.__hour)

        return t1
    
    def add_time(self, t: "Time"):
        self.add_second(t.__second)
        self.add_minute(t.__minute)
        self.add_hour(t.__hour)

