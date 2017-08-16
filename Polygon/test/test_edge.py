import unittest

from poly.edge import Edge
from poly.point import Point
from poly.polygon import Polygon

import random

class TestEdge(unittest.TestCase):

    def test_validEdge(self):
        p = Point(2, 3)
        q = Point(2, 3)
        self.assertEqual(p,q)

        try:
            e = Edge(p,q)
            self.fail("shouldn't allow edge with equal points.")
        except ValueError as e:
            pass

    def test_canIntersectEndPointWithRealIntersection(self):
        e = Edge (Point(0, 0), Point(2, 2))
        f = Edge (Point(-2, 2), Point(2, -2))

        self.assertTrue(e.intersect(f))
        

    def test_nonIntersectEndPoints(self):
        p = Point(0, 0)

        e = Edge (p, Point(2, 3))
        f = Edge (p, Point(-2, 3))

        self.assertIsNone(e.intersect(f))
