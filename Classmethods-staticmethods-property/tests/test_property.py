from unittest import TestCase
from property import Employee as emp


class PropertyTest(TestCase):

    def test_property_getter_fullname_of_employee(self):
        new_employee = emp('Emantsrif', 'Emantsal', 422000)
        fullname_of_new_employee = new_employee.fullname_of_employee
        self.assertEqual(fullname_of_new_employee, 'Emantsrif Emantsal')

    def test_property_setter_fullname_of_employee(self):
        new_employee = emp('Full', 'Stack', 252525)
        new_employee.fullname_of_employee = 'QWERTY YTREWQ'
        self.assertEqual(new_employee.first_name, 'QWERTY')
        self.assertEqual(new_employee.last_name, 'YTREWQ')

    def test_property_deleter_fullname_of_employee(self):
        new_employee = emp('Vasya', 'Pupkin', 140000)
        del new_employee.fullname_of_employee
        self.assertEqual(new_employee.first_name, None)
        self.assertEqual(new_employee.last_name, None)
