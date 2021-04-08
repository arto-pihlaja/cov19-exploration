import unittest
import my_helpers
from datetime import datetime

class TestDateConversion(unittest.TestCase):
    def test_yearwktodate(self):
        self.assertEqual(my_helpers.yearWeekToDateTime('2020-02'), datetime(2020,1,6), 
        "Test 2020Wk1")
        self.assertEqual(my_helpers.yearWeekToDateTime('2020-52'), datetime(2020,12,21), 
        "Test 2020Wk52")
        self.assertEqual(my_helpers.yearWeekToDateTime('2020-53'), datetime(2020,12,28), 
        "Test 2020Wk53")
        self.assertEqual(my_helpers.yearWeekToDateTime('2021-01'), datetime(2021,1,4), 
        "Test 2021Wk1")

if __name__ == "__main__":
    unittest.main()        
