"""
    Defined edge structure.

    An edge is defined by two consecutive points in a polygon.
    Note that an edge only exists with a given polygon, which
    means it is perfectly legitimate to store a 'next' edge
    reference (which would be 'None' in degenerate cases).
"""

from poly.point import Point
from poly.util import value, intersect

class Edge:
    """Represents an edge in Cartesian space."""

    def __init__(self, head, tail):
        """
        Creates an edge for consecutive points head and tail.
        It is assumed that head != tail
        """
        if head == tail:
            raise ValueError("Can't create edge from two identical points")
        self._head = head
        self._tail = tail
        self._next = None

    def setNext(self, e):
        """Make 'e' the next edge in polygon after self."""
        self._next = e

    def next(self):
        """Return next edge in polygon."""
        return self._next

    def copy(self):
        """Return copy of an edge."""
        e = Edge(self._head, self._tail)
        e.next(_next)
        return e

    def head(self):
        """Return head value of edge."""
        return self._head

    def tail(self):
        """Return tail value of edge."""
        return self._tail

    def intersect(self, e):
        """Return intersection between two edges (aside from end-points)."""
        if self.head() == e.head() or self.head() == e.tail():
            return None
        if self.tail() == e.head() or self.tail() == e.tail():
            return None

        # compute intersection of two line segments using x,y coords
        pt = intersect(self.head().x(),
                       self.head().y(),
                       self.tail().x(),
                       self.tail().y(),
                       e.head().x(),
                       e.head().y(),
                       e.tail().x(),
                       e.tail().y())
        if pt is None:
            return None
        return Point (pt[0], pt[1])

    def __str__(self):
        """Return string representation of edge."""
        return "({},{})".format(str(self._head), str(self._tail))

    def __eq__(self, other):
        """Standard equality check."""
        if isinstance(other, self.__class__):
            return self._head == other._head and self._tail == other._tail
        else:
            return False

    def __ne__(self, other):
        """Standard not-equality check."""
        return not self.__eq__(other)

