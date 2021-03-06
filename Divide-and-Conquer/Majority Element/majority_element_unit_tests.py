import unittest
from majority_element import majority_element, majority_element_naive


class TestMajorityElement(unittest.TestCase):
    def test_small(self):
        for elements in [
            [7, 2, 7],
            [7, 8, 9],
            [0,0],
            [0,0,0],
            [1,1,0],
            [0,1,1],
            [1,1,0,0],
            [1,1,1,0],
            [1,0,0,0]
        ]:
            self.assertEqual(
                majority_element(list(elements)),
                majority_element_naive(elements)
            )

    def test_large(self):
        for (elements, answer) in [
            ([0] * 5000 + [1] * 5000, 0)
        ]:
            self.assertEqual(
                majority_element(elements),
                answer
            )


if __name__ == '__main__':
    unittest.main()
