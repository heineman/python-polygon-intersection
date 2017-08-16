"""
    Application to construct sequence of polygons and 
    detect which ones intersect.

    After 3 clicks, a polygon is defined and drawn. Right
    Click to close polygon and then add new one starting
    with left clicks.

    When polygon is added, intersection tests are performed
    by comparing edges.
"""

from poly.polygon import Polygon
from tkinter import Tk, Canvas, ALL

class PolygonApp():
    def __init__(self, master):
        """App to construct polygon by successive left-mouse clicks."""
        
        master.title("Left press to add point to polygon. Right press to start new one.")
        self.master = master 
        
        # keep track of polygons being created
        self.polygons = [Polygon()]
        
        self.canvas = Canvas(master, width=512, height=512)        
        self.canvas.bind("<Button-1>", self.add)
        self.canvas.bind("<Button-2>", self.finalize)
        self.canvas.bind("<Double-Button-1>", self.clear)
        self.canvas.pack()
         
    def toCartesian(self, y):
        """Convert tkinter point into Cartesian."""
        return self.canvas.winfo_height() - y

    def toTk(self,y):
        """Convert Cartesian into tkinter point."""
        return self.canvas.winfo_height() - y

    def add(self, event):
        """Add point to polygon and redraw."""
        self.polygons[0].add (event.x, self.toCartesian(event.y))
        self.visit()

    def finalize(self, event):
        """Finalize polygon and add a new one."""
        self.polygons.insert(0, Polygon())
        self.visit()

    def clear(self, event):
        """Clear all polygons and start again."""
        self.polygons = [Polygon()]
        self.visit()

    def visit (self):
        """Visit structure and represent graphically."""
        self.canvas.delete(ALL)
        n = len(self.polygons)

        # check intersection with all polygons
        colors = [ 'black' ] * n
        for i in range(n-1):
            p = self.polygons[i]
            for j in range(i+1, n):
                q = self.polygons[j]

                if p.valid() and q.valid():
                    if p.intersect(q):
                        colors[i] = colors[j] = 'red'
        
        # now draw all
        for i in range(n-1,-1,-1):
            p = self.polygons[i]

            if p.valid():
                # create single list of (x,y) coordinates
                full = [None] * 2 * p.numEdges()
                idx = 0
                for pt in p:
                    full[idx] = pt.x()
                    full[idx+1] = self.toTk(pt.y())
                    idx += 2
                self.canvas.create_polygon(full, fill=colors[i])
            else:
                for pt in p:
                    self.canvas.create_oval(pt.x()-4, self.toTk(pt.y()-4),
                                            pt.x()+4, self.toTk(pt.y()+4),
                                            fill='gray')
            
if __name__ == '__main__':
    root = Tk()
    app = PolygonApp(root)
    root.mainloop()
