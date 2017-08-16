import unittest

from poly.edge import Edge
from poly.point import Point
from poly.polygon import Polygon
from poly.convex_intersect import convexIntersect
from util import samePolygon
import random

class TestIntersect(unittest.TestCase):

    def test_intersect(self):
        # Note: only works if convex polygons in 
        # normal form, with points/edges in counter-clockwise
        # fashion.
        square = Polygon([
                Point(-2, -2),
                Point(2, -2),
                Point(2, 2),
                Point(-2, 2)])
        triangle = Polygon([
                Point(-2, -2),
                Point(2, -2),
                Point(0, 4)])

        self.assertTrue (triangle.convex())
        self.assertTrue (square.convex())
        p = convexIntersect(square, triangle)
        q = convexIntersect(triangle, square)
        self.assertTrue (samePolygon(p,q))

        real = Polygon([
                Point(2/3, 2),
                Point(-2/3, 2),
                Point(-2, -2),
                Point(2, -2)
                ])
        self.assertTrue (samePolygon(p, real))
        self.assertTrue (samePolygon(real, p))

    def test_intersectNoPointsInCommon(self):
        square = Polygon([
                Point(-2, -2),
                Point(2, -2),
                Point(2, 2),
                Point(-2, 2)])
        triangle = Polygon([
                Point(-3, 0),
                Point(3, 0),
                Point(0, 3)])

        self.assertTrue (triangle.convex())
        self.assertTrue (square.convex())
        p = convexIntersect(square, triangle)
        q = convexIntersect(triangle, square)
        self.assertTrue (samePolygon(p,q))

        real = Polygon([
                Point(2, 0),
                Point(2, 1),
                Point(1, 2),
                Point(-1, 2),
                Point(-2, 1),
                Point(-2, 0)
                ])
        self.assertTrue (samePolygon(p, real))
        self.assertTrue (samePolygon(real, p))

    def test_noIntersection(self):
        """Detect no intersection."""
        square = Polygon([
                Point(-8, -8),
                Point(8, -8),
                Point(8, 8),
                Point(-8, 8)])
        triangle = Polygon([
                Point(23, 0),
                Point(25, 0),
                Point(24, 1)])

        self.assertTrue (triangle.convex())
        self.assertTrue (square.convex())
        p = convexIntersect(square, triangle)
        q = convexIntersect(triangle, square)
        self.assertEqual(p, q)
        self.assertIsNone(p)

    def test_enclosing(self):
        """Detect when polygon wholly contains another polygon."""
        square = Polygon([
                Point(-8, -8),
                Point(8, -8),
                Point(8, 8),
                Point(-8, 8)])
        triangle = Polygon([
                Point(-3, 0),
                Point(3, 0),
                Point(0, 3)])

        self.assertTrue (triangle.convex())
        self.assertTrue (square.convex())
        p = convexIntersect(square, triangle)
        q = convexIntersect(triangle, square)
        self.assertEqual(p, q)

        real = Polygon([
                Point(-3, 0),
                Point(3, 0),
                Point(0, 3)
                ])
        self.assertTrue (samePolygon(p, real))
        self.assertTrue (samePolygon(real, p))

    def test_defective(self):
        """
        This test case detected defect in algorithm. Resolving
        it explained how to choose whether to advance p or q 
        before an intersection had been discovered.
        """
        p = Polygon([
                Point(241,243),
                Point(353,210),
                Point(393,245),
                Point(375,398),
                Point(257,303)])
        q = Polygon([Point(108,189),
                     Point(268,116),
                     Point(456,180),
                     Point(434,226),
                     Point(125,486)
])
        self.assertTrue (p.convex())
        self.assertTrue (q.convex())
        i1 = convexIntersect(p,q)
        i2 = convexIntersect(q,p)
        self.assertTrue(samePolygon(i1, i2))

