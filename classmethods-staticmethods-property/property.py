class Employee:

    """
    A class used to represent an Employee
    ...

    Attributes
    ----------
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

    @property
    def fullname_of_employee(self):
        """
        Returns fullname of employee, using first name and last name.
        :param self: instance of the Employee class
        :type self: instance of the class

        :return: fullname of employee through the space
        :rtype: str
        """
        pass

    @fullname_of_employee.setter
    def fullname_of_employee(self, new_fullname_of_employee):
        """
        Takes new fullname of employee, split it with delimiter ' '.
        Using splitted items changes first name and last name of employee.
        :param self: instance of the Employee class
        :type self: instance of the class

        :param new_fullname_of_employee: new full name of employee
        :type new_fullname_of_employee: str

        :return: nothing
        """
        pass

    @fullname_of_employee.deleter
    def fullname_of_employee(self):
        """
        Takes first name and last name of employee and changes them with None.
        :param self: instance of the Employee class
        :type self: instance of the class

        :return: nothing
        """
        pass
