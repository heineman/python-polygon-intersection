"""
    Construct two random polygons and allow user to move one of them
    around. The frame of the polygons is shown always, but the intersection
    is shown in red.
"""

from poly.polygon import Polygon
from poly.point import Point
from hull.convex import computeHull,computeRandom
from poly.convex_intersect import convexIntersect
from tkinter import Tk, Canvas, ALL


# Ms between refresh events.        
frameDelay = 40

class MovePolygonAnimation():
    def __init__(self, master, p1, p2):
        """
        Create two polygons and allow user to experiment with detecting
        intersections while moving a polygon around.
        """
        master.title("Move the blue-frame polygon to show intersection")
        self.master = master 
        
        self.p1 = p1
        self.p2 = p2
        
        self.canvas = Canvas(master, width=512, height=512)        
        self.canvas.bind("<Button-1>", self.switch)
        self.canvas.bind("<Motion>", self.track)
        self.canvas.pack()
        
        # Register handler which redraws everything at fixed interval
        self.master.after(frameDelay, self.drawEverything)
        
    def toCartesian(self, y):
        """Convert tkinter point into Cartesian."""
        return self.canvas.winfo_height() - y

    def toTk(self,y):
        """Convert Cartesian into tkinter point."""
        return self.canvas.winfo_height() - y

    def track(self, event):
        """Refresh event collection and redraw."""
        anchor = self.p1.get(0)
        deltax = event.x - anchor.x()
        deltay = self.toCartesian(event.y) - anchor.y()
        for p in self.p1:
            p.set(p.x() + deltax, p.y() + deltay)

    def switch(self, event):
        """create two new polygons to use."""
        self.p1 = computeRandom(50, 250, 300, 500)
        self.p2 = computeRandom(50, 250, 300, 500)

    def drawEverything(self):
        """Draw at timed frequency."""
        self.master.after(frameDelay, self.drawEverything)

        self.canvas.delete(ALL)
        self.drawPolygon(self.p1, 'blue', '')
        self.drawPolygon(self.p2, 'black', '')
        intersect = convexIntersect(self.p1, self.p2)
        self.drawPolygon(intersect, '', 'red')

    def drawPolygon(self, p, outline, fill):
        """Draw polygon onto canvas."""
        if p is not None:
            # create single list of (x,y) coordinates
            full = [None] * 2 * p.numEdges()
            idx = 0
            for pt in p:
                full[idx] = pt.x()
                full[idx+1] = self.toTk(pt.y())
                idx += 2
            self.canvas.create_polygon(full, outline=outline, fill=fill)

if __name__ == '__main__':
    p1 = computeRandom(50, 250, 300, 500)
    p2 = computeRandom(50, 250, 300, 500)
    root = Tk()
    app = MovePolygonAnimation(root, p1, p2)
    root.mainloop()
