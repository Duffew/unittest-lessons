import unittest
# import our funtion from evens.py
from evens import even_number_of_evens

# create a class which inherits from the unittest.TestCase class

class TestEvens(unittest.TestCase):
    # define a method beginning with the word 'test' and
    # pass in the 'self' keyword because we are in a class
    def test_function_returns_True(self):
        # now create an assert
        self.assertTrue(even_number_of_evens([]))
    

# run the file without specifying the the unit test module
if __name__ == "__main__":
    unittest.main()