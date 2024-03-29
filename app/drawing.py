from atom import Meta


class Drawing(Meta):
    '''Create graphic elements (graph) including rectangular boxes (which can be square points), 
        ovals (circular points), and segments.
    '''

    def __init__(self, master=None, cnf={}, selector=None, **kw):
        '''Click the left mouse button to start painting, release
            the left mouse button to complete the painting.

        :param selector: The graphics selector, which is an instance of Selector.
        '''
        super().__init__(master, cnf, **kw)
        self.master = master
        self.selector = selector
        self.master.title('Computer Vision')
        self._init_params()
        self._draw_bind()
        
    def _draw_bind(self):
        self.bind("<1>", self.update_xy)
        self.bind("<ButtonRelease-1>", self.draw)

    def _init_params(self):
        self.x = self.y = 0

    def update_xy(self, event):
        '''Press the left mouse button to record the coordinates of the left mouse button'''
        self.x = event.x
        self.y = event.y

    def get_bbox(self, event):
        x0, y0 = self.x, self.y  # The upper-left coordinates of the graph
        x1, y1 = event.x, event.y  # Lower-right coordinates of the graph
        return x0, y0, x1, y1

    def draw(self, event):
        '''Release the left mouse button to finish painting.'''
        self.configure(cursor="arrow")
        bbox = self.get_bbox(event)
        self.create_graph(bbox)

    @property
    def graph_params(self):
        return {
            'width': 5 if 'point' in self.selector.graph_type else 1,
            'tags': self.selector.graph_type,
            'fill': 'red' if 'point' in self.selector.graph_type else None
        }

    def create_graph(self, bbox):
        '''Create a graphic.

        :param bbox: (x0,y0,x1,y1)
        '''
        x0, y0, x1, y1 = bbox
        cond1 = x0 == x1 and y0 == y1 and 'point' not in self.selector.graph_type
        cond2 = 'point' in self.selector.graph_type and (x0 != x1 or y0 != y1)
        if cond1 or cond2:
            return
        else:
            self.draw_graph(self.selector.graph_type.split('_')[0], bbox,
                            color=self.selector.color, **self.graph_params)

    def layout(self, row=0, column=0):
        '''The internal layout.'''
        self.grid(row=row, column=column, sticky='nwes')


class TrajectoryDrawing(Drawing):
    '''Draw based on the mouse's trajectory.
    '''

    def __init__(self, master=None, cnf={}, selector=None, **kw):
        super().__init__(master, cnf, selector, **kw)
        self.bind("<1>", self.update_xy)
        self.bind("<ButtonRelease-1>", self.update_xy)
        self.bind("<Button1-Motion>", self.draw)


def test():
    from tkinter import Tk
    from creator import SelectorFrame
    root = Tk()
    selector = SelectorFrame(root)
    meta = Drawing(root, selector=selector, background='lightgray')
    # Makes the master widget change as the canvas size
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    meta.layout()
    selector.layout()
    selector.grid(row=0, column=1, sticky='nwes')
    root.mainloop()


if __name__ == '__main__':
    test()
