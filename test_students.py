# unittest does not need installing but it does need importing
import unittest

# import the Sutdent class to be tested from student.py
from student import Student

# set up an empty class for the test
class TestStudents(unittest.TestCase):
    
    # define a test to check a 'returns full name method'
    def test_full_name(self):
        # create an instance of the Student class in order to test it
        student = Student('John', 'Doe')
        
        # create an assert to define what we expect to be returned
        self.assertEqual(student.full_name, 'John Doe')

    def test_alert_santa(self):
        # create an instance of the Student class in order to test it
        student = Student('John', 'Doe')
        # with our student instance created, call the alert_santa method on it
        student.alert_santa()
        # test whether student.naughty_list is True
        self.assertTrue(student.naughty_list)


# ensure that the test suite is executed when the file is run as a script
# without having to specify the Unittest module
if __name__ == "__main__":
    unittest.main()