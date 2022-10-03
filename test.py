import unittest

from assignment import valid_date_of_marriage
from assignment import DOB_before_marriage

class unittesting(unittest.TestCase):
    valid_date_of_marriage
    DOB_before_marriage
    def test_check_date_of_marriage(self):
        self.assertEqual(valid_date_of_marriage("20 SEP 2000", "20 SEP 1999"), "Not valid")
    def test_check_DBO_marriage(self):
        self.assertEqual(DOB_before_marriage("20 SEP 2000", "20 SEP 1999"), False)
   