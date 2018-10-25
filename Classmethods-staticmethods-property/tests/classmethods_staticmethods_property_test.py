from unittest import TestCase
from classmethods_staticmethods_property import Employee as emp


class ClassmethodsStaticmethodsPropertyTest(TestCase):

    def test_classmethod_create_new_employee(self):
        """
        Dear bratishka or sestrenka, this test checks your solution in classmethod-create_new_employee
        To pass this test you need true solution in classmethod-create_new_employee
        new_employee type: instance of Employee class
        """
        new_employee = emp.create_new_employee('Edmon-Dantes-10000000')
        self.assertEqual(True, isinstance(new_employee, emp))

    def test_staticmethod_calculate_salary_in_year(self):
        sal = emp.calculate_salary_in_year(5);
        self.assertEqual(sal, 60)

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