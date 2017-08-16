from poly.polygon import Polygon
from poly.point import Point
from poly.util import value,computeAngleSign
import random

""" 
Implement Andrew's Algorithm to compute convex hull for
a collection of points.

Hull must have at least three points to do anything meaningful. If
it does not, then the available points are simply returned as "the hull."
    
This algorithm will still work if duplicate points are found in
the input set of points. The resulting polygon has its points
counterclockwise, thus the interior of the convex polygon is 
"to the left" of each edge.

"""

def lastThreeNonLeft(p):
    """
    Determine if last three points in the polygon form a non-left turn.
    Standard approach (highly sensitive to floating point errors) works
    by computing the determinant of a 3x3 matrix constructed from these
    points.
    """
    if p.numPoints() < 3:
        return False

    x1 = p.get(-3).x()
    y1 = p.get(-3).y()

    x2 = p.get(-2).x()
    y2 = p.get(-2).y()

    x3 = p.get(-1).x()
    y3 = p.get(-1).y()

    sign = computeAngleSign (x1, y1, x2, y2, x3, y3)
    return sign <= 0

def computeHull (points):
    """
    Compute the convex hull for given points and return as polygon.
    Returned polygon is in 'counter-clockwise' fashion, with the 
    interior "to the left" of each edge.
    """
    # sort by x coordinate (and if ==, by y coordinate). 
    n = len(points)
    
    points = sorted(points, key=lambda pt:[pt.x(), pt.y()])
    if n < 3:
        return Polygon(points)
        
    # Compute upper hull by starting with rightmost two points
    upper = Polygon ([points[-1], points[-2]])
    for i in range(n-3, -1, -1):
        upper.add (points[i].x(), points[i].y())

        while upper.numPoints() >=3 and lastThreeNonLeft(upper):
            upper.remove(-2)

    # Compute lower hull by starting with leftmost two points
    lower = Polygon ([points[0], points[1]])
    for i in range(2, n):
        lower.add (points[i].x(), points[i].y())

        while lower.numPoints() >=3 and lastThreeNonLeft(lower):
            lower.remove(-2)
                
    # Merge into upper (skip first and last to avoid duplication) and return.
    upper.remove(-1)
    upper.remove(0)
    for pt in upper:
        lower.add(pt.x(), pt.y())

    return lower

def computeRandom(x, y, u, v):
    """
    Compute random convex polygon within given (x,y), (u,v) bounding area.
    Start from relatively small number of points so polygon has some
    interesting shapes
    """
    points = [Point(random.randint(x,u),random.randint(y,v)) for i in range(10)]
    return computeHull(points)
