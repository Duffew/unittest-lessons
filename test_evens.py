import unittest
# import our funtion from evens.py
from evens import even_number_of_evens

# create a class which inherits from the unittest.TestCase class

class TestEvens(unittest.TestCase):
    # # define a method beginning with the word 'test' and
    # # pass in the 'self' keyword because we are in a class
    # def test_function_returns_True(self):
    #     # now create an assert
    #     self.assertTrue(even_number_of_evens([]))

    # create a function with a name that describes what we are testing
    def test_throws_error_if_value_passed_in_is_not_list(self):
        # write an 'assert' - an 'assert' is what we expect the function to return
        # in this example calling the function even_number_of_evens 
        # with the argument 4 will raise a TypeError
        self.assertRaises(TypeError, even_number_of_evens, 4)

    
    def test_values_in_list(self):
        self.assertEqual(even_number_of_evens([]), False)
        # the next test
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        # what happens if we pass in odd numbers?
        self.assertEqual(even_number_of_evens([1, 3, 5]), False)

# run the file without specifying the the unit test module
if __name__ == "__main__":
    unittest.main()