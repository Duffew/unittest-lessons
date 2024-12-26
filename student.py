from datetime import date, timedelta

class Student:
    """ A Student class as a basis for method testing """
    def __init__(self, first_name, last_name):
        # prepend properties with underscrore to indicate to other devs that these should be read only feilds
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False

    # define the full_name() method as a property
    # The @property decorator in Python is used to define a method as a property. 
    # This allows you to access the method like an attribute, without needing to call it like a function. 
    # It provides a way to implement getter, setter, and deleter functionality for a class attribute 
    # in a concise and readable manner.
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    
    # beacause this is a read-only method, we can we can use the @property decorator
    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"


    # create a method to modify the naughty_list property
    def alert_santa(self):
        self.naughty_list = True

    # code-along challenge
    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=5)


