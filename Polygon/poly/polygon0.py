"""
    Defined polygon structure of points.

    Just bare-bones implementation for presentation
"""

from poly.point import Point
from poly.edge import Edge

class Polygon:
    """Represents polygon of points in Cartesian space."""

    def __init__(self, pts=[]):
        """
        Creates polygon from list of points. If omitted, polygon is empty.
        """
        self.points = []
        for pt in pts:
            self.points.append(pt.copy())

    def copy(self):
        """Return copy of polygon."""
        return Polygon(self.points)

    def add(self, x, y):
        """Extend polygon with additional (x,y) point."""
        self.points.append(Point(x,y))

    def get(self, n):
        """Returns the nth point from polygon (based on zero)."""
        return self.points[n]

    def remove(self, n):
        """Delete the nth point from polygon (based on zero)."""
        del self.points[n]

    def numPoints(self):
        """Return the number of points in polygon."""
        return len(self.points)

    def numEdges(self):
        """Return the number of edges in polygon."""
        if len(self.points) < 1:
            return 0
        elif len(self.points) == 2:
            return 1
        else:
            return len(self.points)

    def valid(self):
        """A polygon becomes valid with three or more points."""
        return len(self.points) >= 3

    def __iter__(self):
        """Return points in the polygon in order."""
        for pt in self.points:
            yield pt

    def edges(self):
        """Return edges in the polygon, in order."""
        order = []
        for i in range(0, len(self.points)-1):
            order.append(Edge(self.points[i], self.points[i+1]))

        if self.valid():
            n = len(self.points)
            order.append(Edge(self.points[n-1], self.points[0]))

        # Now link edges to next one in the chain. Make sure to
        # link back to start
        for i in range(len(order)-1):
            order[i].setNext(order[i+1])
        order[-1].setNext(order[0])
        return order
                             
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.points == other.points
        else:
            return False

