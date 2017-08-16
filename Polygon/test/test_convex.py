import unittest

from poly.edge import Edge
from poly.point import Point
from poly.polygon import Polygon

import random

class TestConvex(unittest.TestCase):

    def test_nonConvexShape(self):
        p = Polygon([Point(-2, 2),
                     Point(0, -2),
                     Point(2, 2),
                     Point(0,0)])
        self.assertFalse(p.convex())

    def test_simpleonvexShape(self):
        p = Polygon([Point(-2, 2),
                     Point(0, -2),
                     Point(2, 2)])
        self.assertTrue(p.convex())

