import unittest
from CalculateDueDateModule import CalculateDueDate as calculate
from datetime import datetime


class MyTestCase(unittest.TestCase):

    def test_CalculateDueDate(self):
        self.assertEqual(calculate(datetime.strptime('2019-08-16T11:41:24+0200' , "%Y-%m-%dT%H:%M:%S%z"),8),datetime.strptime('2019-08-19 11:41:24',"%Y-%m-%d %H:%M:%S"))
        self.assertEqual(calculate(datetime.strptime('2019-08-16T14:00:00+0200', "%Y-%m-%dT%H:%M:%S%z"), 24),datetime.strptime('2019-08-21 14:00:00', "%Y-%m-%d %H:%M:%S"))
        self.assertEqual(calculate(datetime.strptime('2019-08-16T14:00:00+0200', "%Y-%m-%dT%H:%M:%S%z"), 4),datetime.strptime('2019-08-19 10:00:00', "%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
    unittest.main()
