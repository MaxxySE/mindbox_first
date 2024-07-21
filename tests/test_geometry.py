import unittest
import math
from geometry import Circle, Triangle, Square, calculate_area


class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_triangle_is_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

    def test_square_area(self):
        square = Square(4)
        self.assertAlmostEqual(square.area(), 16)

    def test_square_is_right(self):
        square = Square(4)
        self.assertTrue(square.is_right())

    def test_calculate_area(self):
        shapes = [Circle(5), Triangle(3, 4, 5), Square(4)]
        areas = [calculate_area(shape) for shape in shapes]
        expected_areas = [math.pi * 25, 6, 16]
        for area, expected in zip(areas, expected_areas):
            self.assertAlmostEqual(area, expected)


if __name__ == '__main__':
    unittest.main()
