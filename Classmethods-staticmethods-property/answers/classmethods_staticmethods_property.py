class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def create_new_employee(cls, new_employee_string):
        first_name, last_name, salary = new_employee_string.split('-')
        return cls(first_name, last_name, salary)

    @staticmethod
    def calculate_salary_in_year(salary_in_month):
        salary_in_year = salary_in_month * 12
        return salary_in_year

    @property
    def fullname_of_employee(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @fullname_of_employee.setter
    def fullname_of_employee(self, new_fullname_of_employee):
        self.first_name, self.last_name = new_fullname_of_employee.split(' ')

    @fullname_of_employee.deleter
    def fullname_of_employee(self):
        self.first_name = None
        self.last_name = None
        print('Name was deleted!')
