"""
    Utility functions for testing.

    To aid testing, we need to compare two polygons to make 
    sure they are "the same". This is more than the __eq__
    method was meant for. These are quick and dirty, but 
    should do the trick.
"""

from poly.polygon import Polygon
from poly.edge import Edge
from poly.util import value

def samePoint(u, v):
    """
    Returns False if points are different. True if they seem
    identical. Use 'value' method from poly.util.
    """
    return value(u.x() - v.x()) == 0 and value(u.y() - v.y()) == 0

def sameEdge(p, q):
    """
    Returns False if edges are different. True if they seem
    identical. Use 'value' method from poly.util.
    """
    return samePoint(p.head(), q.head()) and samePoint(p.tail(), q.tail())

def samePolygon(p, q):
    """
    Returns False if polygons are different. True if they seem 
    identical. Use 'value' method from poly.util
    """
    copyp = p.copy()
    copyq = q.copy()
    if p is q:
        return True
    if p.numPoints() != q.numPoints():
        return False

    # Circle through edges at least N times until the
    # first edge of pe matches first in qe
    pe = p.edges()
    qe = q.edges()
    n  = p.numPoints() + 1
    while not sameEdge(pe[0],qe[0]) and n > 0:
        pe.append(pe.pop(0))
        n -= 1

    # if not able to align, then false
    if n == 0:
        return False

    # matched first edge, what about rest...
    for i in range(len(pe)):
        if not sameEdge(pe[i], qe[i]):
            return False

    return True
