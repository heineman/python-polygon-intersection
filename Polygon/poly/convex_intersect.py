from poly.polygon import Polygon
from poly.point import Point
from poly.util import value,computeAngleSign
from math import degrees, acos, sqrt

""" 
Implement Convex Polygon Intersection algorithm 
[O'Rourke, Chien, Olson, Naddor, 1982]
https://pdfs.semanticscholar.org/3a68/0593c409eb0d86a9c436113581df970554ba.pdf

Note that this algorithm only works on convex polygons.

In general assumes that whenever two edges intersect, they intersect
in a single point that is not a vertex of exither polygon. Might not
handle some really special cases, as described in the above paper.
"""

def inhalfplane(pt, q):
    """Return True if point pt is in half-plane defined by q."""
    signTail = computeAngleSign(pt.x(), pt.y(),
                                q.head().x(), q.head().y(),
                                q.tail().x(), q.tail().y())
    return signTail >= 0

def aim (p, q):
    """Return true if p is "aiming towards" q's half-plane edge."""
    # First check if p.tail is in the half-plane of q
    inside = inhalfplane(p.tail(), q)

    # compute cross product of q x p to determine orientation
    # en.wikipedia.org/wiki/Cross_product#Computational_geometry
    # normalize p and q
    pnorm = Point(p.tail().x() - p.head().x(), 
                  p.tail().y() - p.head().y())
    qnorm = Point(q.tail().x() - q.head().x(), 
                  q.tail().y() - q.head().y())

    cross = qnorm.x()*pnorm.y() - qnorm.y()*pnorm.x()
    if inside:
        # in half-plane, so now check orientation
        return cross < 0
    else:
        # not in half-plane.
        return cross >= 0

def dist(p, q):
    """Compute Euclidean distance between two points."""
    return sqrt((p.x()-q.x())**2 + (p.y()-q.y())**2)

def containedWithin(pt, p):
    """
    Determine if pt is fully contained within p. Do so by 
    summing angles with each edge in the convex polygon p.
    """
    sum = 0
    for e in p.edges():
        C = dist(e.head(), e.tail())
        A = dist(pt, e.head())
        B = dist(pt, e.tail())
        sum += degrees(acos((A*A+B*B-C*C)/(2*A*B)))
    return value(sum-360) == 0

def convexIntersect(p, q):
    """
    Compute and return polygon resulting from the intersection of
    two convext polygons, p and q.
    """
    intersection = Polygon()
    pn = p.numEdges()
    qn = q.numEdges()
    k = 1
    inside = None              # can't know inside until intersection
    first = None               # remember 1st intersection to know when to stop
    firstp = pe = p.edges()[0] # get first edge of p and q
    firstq = qe = q.edges()[0]
    while k < 2*(pn + qn):
        pt = pe.intersect(qe)
        if pt is not None:
            if first == None:
                first = pt
            elif pt == first:
                # stop when find first intersection again
                break

            intersection.add(pt.x(), pt.y())
            if inhalfplane(pe.tail(), qe):
                inside = p
            else:
                inside = q

        # Identify relationship between edges; either we advance
        # p or we advance q, based on whether p's current edge
        # is aiming at qe (or vice versa).
        advancep = advanceq = False

        if (aim(pe,qe) and aim(qe,pe)) or (not aim(pe,qe) and not aim(qe,pe)):
            if inside is p:
                advanceq = True
            elif inside is q:
                advancep = True
            else:
                # no intersection yet. Choose based on
                # which one is "outside"
                if inhalfplane(pe.tail(), qe):
                    advanceq = True
                else:
                    advancep = True
        elif aim(pe, qe):
            advancep = True
        elif aim(qe, pe):
            advanceq = True

##        if aim(pe, qe):
##            if aim(qe, pe):
##                if inside is p:
##                    advanceq = True
##                elif inside is q:
##                    advancep = True
##                else:
##                    advancep = True    # arbitrary pick
##            else:
##                advancep = True
##        else:
##            if aim(qe, pe):
##                advanceq = True
##            else:
##                if inside is p:
##                    advanceq = True
##                elif inside is q:
##                    advancep = True
##                else:
##                    advancep = True    # arbitrary pick

        if advancep:
            if inside is p:
                intersection.add(pe.tail().x(), pe.tail().y())
            pe = pe.next()
        elif advanceq:
            if inside is q:
                intersection.add(qe.tail().x(), qe.tail().y())
            qe = qe.next()

        k += 1
            
    if intersection.numPoints() == 0:
        if containedWithin(firstp.tail(), q):
            return p
        elif containedWithin(firstq.tail(), p):
            return q
        else:
            return None

    # Return computed intersection
    return intersection
