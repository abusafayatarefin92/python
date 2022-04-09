import unittest
from employee import Employee
from unittest.mock import patch


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Khurshid', 'Alam', 50000)
        self.emp_2 = Employee('Sakib', 'Khan', 50000)

    def tearDown(self):
        print('tearDown\n')
        pass

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Khurshid.Alam@email.com')
        self.assertEqual(self.emp_2.email, 'Sakib.Khan@email.com')

        self.emp_1.first = 'Riyad'
        self.emp_2.first = 'Rakib'

        self.assertEqual(self.emp_1.email, 'Riyad.Alam@email.com')
        self.assertEqual(self.emp_2.email, 'Rakib.Khan@email.com')

    def test_fullname(self):
        print("test_fullname")
        self.assertEqual(self.emp_1.fullname, 'Khurshid Alam')
        self.assertEqual(self.emp_2.fullname, 'Sakib Khan')

        self.emp_1.first = 'Riyad'
        self.emp_2.first = 'Rakib'

        self.assertEqual(self.emp_1.fullname, 'Riyad Alam')
        self.assertEqual(self.emp_2.fullname, 'Rakib Khan')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.applyraise()
        self.emp_2.applyraise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 52500)

    def test_monthly_schedule(self):
        print('test_monthly_schedule')
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Alam/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Khan/June')
            self.assertEqual(schedule, 'Bad response!')


if __name__ == '__main__':
    unittest.main()
