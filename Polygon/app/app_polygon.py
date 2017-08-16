"""
    Application to construct polygon using left mouse clicks.

    After 3 clicks, a polygon is defined and drawn.    
"""

from poly.polygon import Polygon
from tkinter import Tk, Canvas, ALL

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

def color(c):
    """Return color from palette, up to maximum."""
    return colors[min(c, len(colors)-1)]

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
        self.canvas.pack()
         
    def add(self, event):
        """Add point to polygon and redraw."""
        self.polygons[0].add (event.x, event.y)
        self.visit()

    def finalize(self, event):
        """Finalize polygon and add a new one."""
        self.polygons.insert(0, Polygon())
        self.visit()

    def visit (self):
        """Visit structure and represent graphically."""
        self.canvas.delete(ALL)
        c = len(self.polygons)-1
        for p in self.polygons:
            if p.valid():
                # create single list of (x,y) coordinates
                full = [None] * 2 * p.numEdges()
                idx = 0
                for pt in p:
                    full[idx] = pt.x()
                    full[idx+1] = pt.y()
                    idx += 2
                self.canvas.create_polygon(full, fill=color(c))
            else:
                for pt in p:
                    self.canvas.create_oval(pt.x()-4, pt.y()-4, 
                                            pt.x()+4, pt.y()+4, fill='gray')
            c -= 1
            
            
if __name__ == '__main__':
    root = Tk()
    app = PolygonApp(root)
    root.mainloop()
