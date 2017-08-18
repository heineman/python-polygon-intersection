import unittest

from poly.edge import Edge
from poly.point import Point
from poly.polygon import Polygon
from poly.convex_intersect import convexIntersect
from util import samePolygon

class TestSlide(unittest.TestCase):


    def test_slide(self):
        """Example to use with slide presentation."""
        square = Polygon([
                Point(0, 8),
                Point(0, 0),
                Point(8, 0),
                Point(8, 8)])
        triangle = Polygon([
                Point(8, 10),
                Point(4, 6),
                Point(12, 6)])

        self.assertTrue (triangle.convex())
        self.assertTrue (square.convex())
        p = convexIntersect(square, triangle)
        q = convexIntersect(triangle, square)
        self.assertEqual(p, q)

        real = Polygon([
                Point(8, 6),
                Point(8, 8),
                Point(6, 8),
                Point(4, 6)
                ])
        self.assertTrue (samePolygon(p, real))
        self.assertTrue (samePolygon(real, p))
