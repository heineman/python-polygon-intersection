"""
    Defined point structure.

    Constructing a point class makes it possible to easily
    query or modify points in a polygon.
"""

class Point:
    """Represents a point in Cartesian space."""

    def __init__(self, x, y):
        """Creates a point (x,y) in Cartesian space."""
        self._x = x
        self._y = y

    def copy(self):
        """Return copy of a point."""
        return Point(self._x, self._y)

    def x(self):
        """Return x value of point."""
        return self._x

    def y(self):
        """Return y value of point."""
        return self._y

    def set(self, x, y):
        """Update the (x,y) values for a Point."""
        self._x = x
        self._y = y

    def __str__(self):
        """Return string representation of point."""
        return "({},{})".format(self._x, self._y)

    def __eq__(self, other):
        """Standard equality check."""
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        """Standard not-equality check."""
        return not self.__eq__(other)
