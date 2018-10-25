"""
Dear bratishka or sestrenka, We hope you have some knowledge about classmethods, staticmethods, property.
In any case, these are small explanations on these topics.
Classmethod:
    The @classmethod decorator, is a builtin function decorator that is an expression that gets evaluated after your function is defined. The result of that evaluation shadows your function definition.
    A class method receives the class as implicit first argument, just like an instance method receives the instance
    Syntax:
    class C(object):
        @classmethod
        def fun(cls, arg1, arg2, ...):
        ....
    fun: function that needs to be converted into a class method
    returns: a class method for function.
    -A class method is a method which is bound to the class and not the object of the class.
    -They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
    -It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that will be applicable to all the instances

Staticmethod:
    A static method does not receive an implicit first argument.
    Syntax:

    class C(object):
        @staticmethod
        def fun(arg1, arg2, ...):
            ...
    returns: a static method for function fun.
    -A static method is also a method which is bound to the class and not the object of the class.
    -A static method can’t access or modify class state.
    -It is present in a class because it makes sense for the method to be present in class.

Property:
    Getters and setters are used in many object oriented programming languages to ensure the principle of data encapsulation(is seen as the bundling of data with the methods that operate on these data.)
    These methods are of course the getter for retrieving the data and the setter for changing the data.
    According to this principle, the attributes of a class are made private to hide and protect them from other code.
    @property is basically a pythonic way to use getters and setters.
    Python has a great concept called property which makes the life of an object-oriented programmer much simpler.

P.S. Don't be upset, if not everything is clear. Google will help you
"""


class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    @classmethod
    def create_new_employee(cls, new_employee_string):
        """
        Dear bratishka or sestrenka
        :param new_employee_string:
        :return:
        """
        pass

    @staticmethod
    def calculate_salary_in_year(salary_in_month):
        pass

    @property
    def fullname_of_employee(self):
        pass

    @fullname_of_employee.setter
    def fullname_of_employee(self, new_fullname_of_employee):
        pass

    @fullname_of_employee.deleter
    def fullname_of_employee(self):
        pass
