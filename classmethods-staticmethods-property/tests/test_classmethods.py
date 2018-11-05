from unittest import TestCase
from classmethods import Employee as emp


class ClassmethodsTest(TestCase):

    def test_classmethod_create_new_employee(self):
        new_employee = emp.create_new_employee('Edmon-Dantes-10000000')
        self.assertEqual(True, isinstance(new_employee, emp))

    def test_classmethod_change_working_place(self):
        new_employee = emp('Naruto', 'Uzumaki', 422000)
        emp.change_working_place('Google')
        self.assertEqual(new_employee.working_place, 'Google')
