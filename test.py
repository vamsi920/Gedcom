import unittest

from assignment import valid_date_of_marriage
from assignment import DOB_before_marriage
from assignment import valid_date_of_birth_current
from assignment import DOB_after_Death
from assignment import valid_divorce_before_death
from assignment import ageBelow100

class unittesting(unittest.TestCase):
    def test_check_date_of_marriage(self):
        self.assertEqual(valid_date_of_marriage("20 SEP 2000", "20 SEP 1999"), "Not valid")
    def test_check_DBO_marriage(self):
        self.assertEqual(DOB_before_marriage("20 SEP 2000", "20 SEP 1999"), False)
    
    def test_check_current_dob(self):
        self.assertEqual(valid_date_of_birth_current("03 OCT 2022", "25 MAR 2000"), "Not valid")
    def test_check_DOB_Death(self):
        self.assertEqual(DOB_after_Death("11 OCT 2001", "26 FEB 2003"), True)

    def test_valid_divorce_before_death(self):
        self.assertEqual(valid_divorce_before_death("03 OCT 2022", "25 MAR 2000"), False)
    def test_ageBelow100(self):
        self.assertEqual(ageBelow100("11 OCT 2001"), True)
   