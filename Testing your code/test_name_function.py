
import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    ### Test for 'name_function
    def test_first_last_name(self):
        formatted_name = get_formatted_name('Janis','Joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()       