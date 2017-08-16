import unittest

from poly.edge import Edge
from poly.point import Point
from poly.polygon import Polygon

import random

class TestPolygon(unittest.TestCase):

    def test_weakSimple(self):
        """See Wikipedia for entry on weakly simple polygon."""
        m = Point(0, 0)
        a = Point(0, 4)
        b = Point(8, 4)
        c = Point(8, 0)
        d = Point(4, 0)
        e = Point(4, 1)
        f = Point(6, 1)
        g = Point(6, 3)
        h = Point(2, 3)
        j = Point(2, 1)
        k = Point(4, 1)  # same as e
        l = Point(4, 0)  # same as d
        p = Polygon([a, b, c, d, e, f, g, h, j, k, l, m])
        self.assertTrue(p.simple())

    def test_nonIntersectSimplePolygonsOnEndPoints(self):
        a = Point(0, 0)
        b = Point(-2, 2)
        c = Point(2, 2)

        d = Point(-2, -2)
        e = Point(2, -2)

        p = Polygon([a, b, c])
        q = Polygon([a, d, e])

        self.assertFalse(p.intersect(q))

    def test_canIntersectEndPointWithRealIntersection(self):
        e = Edge (Point(0, 0), Point(2, 2))
        f = Edge (Point(-2, 2), Point(2, -2))

        self.assertTrue(e.intersect(f))
        

    def test_nonIntersectEndPoints(self):
        p = Point(0, 0)

        e = Edge (p, Point(2, 3))
        f = Edge (p, Point(-2, 3))

        self.assertIsNone(e.intersect(f))
