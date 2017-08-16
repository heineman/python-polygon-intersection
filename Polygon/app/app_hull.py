"""
    Application to construct a convex hull for points being added.

    Right-click to refresh
"""

from poly.polygon import Polygon
from poly.point import Point
from hull.convex import computeHull
from tkinter import Tk, Canvas, ALL

class HullApp():
    def __init__(self, master):
        """App to construct polygon by successive left-mouse clicks."""
        
        master.title("Left press to add point to polygon. Right press to start new one.")
        self.master = master 
        
        # keep track of points being created
        self.points = []
        
        self.canvas = Canvas(master, width=512, height=512)        
        self.canvas.bind("<Button-1>", self.add)
        self.canvas.bind("<Button-2>", self.clear)
        self.canvas.pack()
         
    def toCartesian(self, y):
        """Convert tkinter point into Cartesian."""
        return self.canvas.winfo_height() - y

    def toTk(self,y):
        """Convert Cartesian into tkinter point."""
        return self.canvas.winfo_height() - y
         
    def add(self, event):
        """Add point to polygon and redraw."""
        self.points.append (Point(event.x, self.toCartesian(event.y)))
        self.visit()

    def clear(self, event):
        """Clear all polygons and start again."""
        self.points = []
        self.visit()

    def visit (self):
        """Visit structure and represent graphically."""
        self.canvas.delete(ALL)

        p = computeHull(self.points)
        if p.valid():
            # create single list of (x,y) coordinates
            full = [None] * 2 * p.numEdges()
            idx = 0
            for pt in p:
                full[idx] = pt.x()
                full[idx+1] = self.toTk(pt.y())
                idx += 2
                self.canvas.create_polygon(full, fill='lightGreen')

        # show points in gray
        for pt in self.points:
            self.canvas.create_oval(pt.x()-4, self.toTk(pt.y()-4),
                                    pt.x()+4, self.toTk(pt.y()+4),
                                    fill='gray')
            
if __name__ == '__main__':
    root = Tk()
    app = HullApp(root)
    root.mainloop()
