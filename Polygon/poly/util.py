"""
    Utility functions.

    The intersect method will generate floating point values, and as 
    such, may introduce small errors because of precision errors.
"""

epsilon = 1E-9

def value(x):
    """Returns 0 if x is 'sufficiently close' to zero, +/- 1E-9"""
    if x >= 0 and x <= epsilon:
        return 0
    if x < 0 and -x <= epsilon:
        return 0
    return x

def computeAngleSign(x1, y1, x2, y2, x3, y3):
    """
    Determine if angle (p1,p2,p3) is right or left turn by computing
    3x3 determinant. If sign is + if p1-p2-p3 forms counterclockwise
    triangle. So if positive, then left turn. If zero then colinear.
    If negative, then right turn.
    """
    val1 = (x2 - x1)*(y3 - y1)
    val2 = (y2 - y1)*(x3 - x1)
    diff = value(val1 - val2)
    if diff > 0:
        return +1
    elif diff < 0:
        return -1
    else:
        return 0

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Return the point of intersection (or None) between edges:

      e1: (x1,y1) - (x2,y2)
      e2: (x3,y3) - (x4,y4)

    Might include end-points.
    """
    # common denominator
    da = (y4 - y3)*(x2 - x1)
    db = (x4 - x3)*(y2 - y1)
    denom = da - db
                
    if value(denom) == 0:
        return None    # PARALLEL OR COINCIDENT
                
    # numerators
    ux = (x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)
    uy = (x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)
                
    ux = ux / denom
    uy = uy / denom
                
    # line segment intersections are between 0 and 1. Both must be true
    # Special care on both boundaries w/ floating point issues.
    if value(ux) >= 0 and value(ux-1) <= 0 and value(uy) >= 0 and value(uy-1) <= 0:
        ix = x1 + ux*(x2-x1)
        iy = y1 + ux*(y2-y1)
        return (ix, iy)
        
    return None     # no intersection

