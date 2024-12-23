import unittest
from rectangle_area import rectangle_area


class TestRectangleArea(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(rectangle_area(5, 10), 50)

    def test_zero_length(self):
        with self.assertRaises(ValueError):
            rectangle_area(0, 10)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            rectangle_area(5, -3)

    def test_floats(self):
        self.assertAlmostEqual(rectangle_area(5.5, 4.2), 23.1, places=1)


if __name__ == "__main__":
    unittest.main()
