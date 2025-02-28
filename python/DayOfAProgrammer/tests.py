import unittest

from DayOfAProgrammer import dayOfProgrammer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Test case 1: Gregorian non-leap year
        self.assertEqual("13.09.2017", dayOfProgrammer(2017))

        # Test case 2: Gregorian leap year
        self.assertEqual("12.09.2016", dayOfProgrammer(2016))

        # Test case 3: Julian leap year
        self.assertEqual("12.09.1800", dayOfProgrammer(1800))

        # Test case 4: Transition year
        self.assertEqual("26.09.1918", dayOfProgrammer(1918))


if __name__ == '__main__':
    unittest.main()
