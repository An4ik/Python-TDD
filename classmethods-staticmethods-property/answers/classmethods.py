
class Employee:

    working_place = "SDU"

    """
    A class used to represent an Employee
    ...
    Attributes
    ----------
    working_place : str
        class variable, working place for all existing employees
    first_name : str
        a first name of employee
    last_name : str
        a last name of employee
    salary : int
        a salary of employee
    """

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def create_new_employee(cls, new_employee_string):
        """
        A class method receives the class as implicit first argument,
        just like an instance method receives the instance.
        Method takes new_employee_string, which consist of first name, last name, salary,
        and split it with delimiter '-'.
        Using splitted items creates a class object new employee and returns it.
        :param cls: Employee class
        :type cls: class

        :param new_employee_string: which contains employee's data(first name, last name, salary)
        :type new_employee_string: string

        :return: new created object of Employee
        :rtype: instance of the class
        """
        first_name, last_name, salary = new_employee_string.split('-')
        return cls(first_name, last_name, salary)

    @classmethod
    def change_working_place(cls, new_working_place):
        """
        Takes new_working_place variable and changes with it class variable working_place.
        For all employees would be new working place.
        :param new_working_place: working place of all employees
        :type new_working_place: str
        :return: nothing
        """
        cls.working_place = new_working_place


