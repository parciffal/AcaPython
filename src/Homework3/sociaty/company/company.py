from ...date_time.my_date.my_date import Date


class Company:

    def __init__(self, company_name: str,
                 founded_at: Date,
                 employees_count: int):
        self.__company_name = company_name
        self.__founded_at = founded_at
        self.__employees_count = employees_count

    @property
    def company_name(self):
        return self.__company_name

    @company_name.setter
    def company_name(self, value: str):
        self.__company_name = value

    @property
    def founded_at(self):
        return self.__founded_at

    @founded_at.setter
    def founded_at(self, value: Date):
        self.__founded_at = value

    @property
    def employees_count(self):
        return self.__employees_count

    @employees_count.setter
    def employees_count(self, value: int):
        self.__employees_count = value

    def __repr__(self) -> str:
        return "Name: {}\n" \
               "Founded at: {}\n" \
               "Employees Count: {}" \
            .format(self.company_name,
                    self.founded_at.__repr__(),
                    self.employees_count)

    def add_employee(self):
        self.employees_count += 1

    def del_employee(self):
        self.employees_count -= 1
