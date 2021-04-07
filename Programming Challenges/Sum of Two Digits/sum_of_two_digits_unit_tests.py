import unittest
from itertools import product
from sum_of_two_digits import sum_of_two_digits, is_even


class TestSumOfTwoDigits(unittest.TestCase):
    def test_all_inputs(self):
        for first_digit, second_digit in product(range(10), repeat=2):
            self.assertEqual(sum_of_two_digits(first_digit, second_digit), first_digit + second_digit)

    def test_numbers(self):
        self.assertEqual(is_even([1, 4, 5, 2, 0, 8, 3, 6, 7]), False)
        self.assertEqual(is_even([0, 3, 2, 4, 5, 6, 7, 1, 9, 8]), True)
        self.assertEqual(is_even([0, 3, 4, 1, 2]), True)


if __name__ == '__main__':
    unittest.main()
