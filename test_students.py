# unittest does not need installing but it does need importing
import unittest

# import the Sutdent class to be tested from student.py
from student import Student
from datetime import timedelta

# set up an empty class for the test
class TestStudents(unittest.TestCase):

    # setUp the testing environment and create an instance of the entire class
    @classmethod
    def setUpClass(cls):
        print("set up class")

    # setUp the testing environment and create an instance of the student
    # add print statements to see when setUp and tearDown appear within
    # the testing sequence
    def setUp(self):
        print("setUp")
        self.student = Student('John', 'Doe')

    
    @classmethod
    def tearDownClass(cls):
        print("tear down Class")


    def tearDown(self):
        print("tearDown")

    # define a test to check a 'returns full name method'
    def test_full_name(self):
        print("test_full_name")
        # create an instance of the Student class in order to test it
        # removed when using setUp and tearDown
        # student = Student('John', 'Doe')
        
        # create an assert to define what we expect to be returned
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        print("test_alert_santa")
        # create an instance of the Student class in order to test it
        # student = Student('John', 'Doe')
        # with our student instance created, call the alert_santa method on it
        self.student.alert_santa()
        # test whether student.naughty_list is True
        self.assertTrue(self.student.naughty_list)

    
    def test_email(self):
        print("test_email")
        # student = Student('John', 'Doe')
        
        self.assertEqual(self.student.email, 'john.doe@email.com')


    # code-along challenge
    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

# ensure that the test suite is executed when the file is run as a script
# without having to specify the Unittest module
if __name__ == "__main__":
    unittest.main()