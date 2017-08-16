"""
    Application to plot two polygons drawn from two input files
    and to compute their intersection.

    Right-click to refresh
"""
import sys

from poly.polygon import Polygon
from poly.point import Point
from hull.convex import computeHull,computeRandom
from poly.convex_intersect import convexIntersect
from tkinter import Tk, Canvas, ALL

# default values for regions where random polygons are constructed
v1 = 100
v2 = 300    # random polygon in (100,100) - (300,300)
v3 = 200
v4 = 400    # random polygon in (200,200) - (400,400)

class IntersectingPolygons():
    def __init__(self, master, p1, p2):
        """Show two polygons on the screen, with intersection."""
        
        master.title("Two polygons with their intersection")
        self.master = master 
        
        self.p1 = p1
        self.p2 = p2
        self.intersection = None
        
        self.canvas = Canvas(master, width=512, height=512)        
        self.canvas.bind("<Button-1>", self.showFull)
        self.canvas.bind("<Button-2>", self.showPoly)
        self.canvas.pack()
        self.canvas.bind("<Configure>", self.drawPolygons)

    def drawPolygons(self, event):
        """Once screen ready to draw, do it."""
        self.drawPolygon(self.p1, 'purple')
        self.drawPolygon(self.p2, 'blue')
         
    def toCartesian(self, y):
        """Convert tkinter point into Cartesian."""
        return self.canvas.winfo_height() - y

    def toTk(self,y):
        """Convert Cartesian into tkinter point."""
        return self.canvas.winfo_height() - y

    def drawPolygon(self, p, fill):
        """Draw polygon onto canvas."""
        if p is None:
            self.intersection = Polygon()
            self.canvas.create_text(self.canvas.winfo_width()/2,
                                    self.canvas.winfo_height()/2,
                                    text='no intersection',
                                    fill=fill)
        else:
            # create single list of (x,y) coordinates
            full = [None] * 2 * p.numEdges()
            idx = 0
            for pt in p:
                full[idx] = pt.x()
                full[idx+1] = self.toTk(pt.y())
                idx += 2
            self.canvas.create_polygon(full, fill=fill)

            # show points in gray
            for pt in p:
                self.canvas.create_oval(pt.x()-4, self.toCartesian(pt.y()-4),
                                        pt.x()+4, self.toCartesian(pt.y()+4),
                                        fill='gray')

    def showPoly (self, event):
        """If showing intersection, go back to just poly."""
        self.canvas.delete(ALL)
        self.intersection = None
        self.drawPolygons(None)


    def showFull (self, event):
        """Show Intersection or generate new polygons."""
        if self.intersection is None:
            self.intersection = convexIntersect(self.p1, self.p2)
            self.drawPolygon(self.intersection, 'red')
        else:
            self.canvas.delete(ALL)
            self.p1 = computeRandom(v1, v1, v2, v2)
            self.p2 = computeRandom(v3, v3, v4, v4)
            self.drawPolygons(None)
            self.intersection = None
            
if __name__ == '__main__':
    # generate two random polygons
    if len(sys.argv) >= 4:
        v1 = int(sys.argv[1])
        v2 = int(sys.argv[2])
        v3 = int(sys.argv[3])
        v4 = int(sys.argv[4])

    p1 = computeRandom(v1, v1, v2, v2)
    p2 = computeRandom(v3, v3, v4, v4)

    root = Tk()
    app = IntersectingPolygons(root, p1, p2)
    root.mainloop()
