'''Use help reference at https://www.jianshu.com/p/c6a2b400d0b9
'''
from tkinter import ttk, StringVar

from atom import Meta
from param import Param


class Selector(Meta):
    colors = 'red', 'blue', 'black', 'purple', 'green', 'skyblue', 'yellow', 'white'
    shapes = 'rectangle', 'oval', 'line', 'oval_point', 'rectangle_point'

    def __init__(self, master=None, cnf={}, **kw):
        '''The base class of all graphics frames.

        :param master: a widget of tkinter or tkinter.ttk.
        '''
        super().__init__(master, cnf, **kw)
        self.start, self.end = 15, 50
        self.create_color()
        self.create_shape()

    def create_color(self):
        '''Set the color selector'''
        self.create_text((self.start, self.start),
                         text='color', font='Times 15', anchor='w')
        self.start += 10
        for k, color in enumerate(Selector.colors):
            t = 7+30*(k+1)
            direction = self.start+t, self.start-20, self.end+t, self.end-20
            self.draw_graph('rectangle', direction,
                            'yellow', tags=color, fill=color)
        self.dtag('rectangle')

    def create_shape(self):
        '''Set the shape selector'''
        self.create_text((self.start-10, self.start+30),
                         text='shape', font='Times 15', anchor='w')
        for k, shape in enumerate(Selector.shapes):
            t = 7+30*(k+1)
            direction = self.start+t, self.start+20, self.end+t, self.end+20
            width = 10 if shape == 'line' else 1
            fill = 'blue' if 'point' in shape else 'white'
            self.draw_graph(shape.split(
                '_')[0], direction, 'blue', width=width, tags=shape, fill=fill)


class SelectorFrame(ttk.Frame):
    def __init__(self, master=None, **kw):
        '''The base class of all graphics frames.

        :param master: a widget of tkinter or tkinter.ttk.
        '''
        super().__init__(master, **kw)
        self.color = None
        self.graph_type = None
        self.selector = Selector(self, background='lightgreen')
        [self.color_bind(self.selector, color) for color in Selector.colors]
        [self.graph_type_bind(self.selector, graph_type)
         for graph_type in Selector.shapes]
        self.selector.dtag('all')
        self.info_var = StringVar()
        self.info = ttk.Label(self, textvariable=self.info_var)

    def update_info(self):
        if self.color or self.graph_type:
            text = f"You Selected: {self.color},{self.graph_type}"
            self.info_var.set(text)

    def set_color(self, new_color):
        self.color = new_color
        self.update_info()

    def set_graph_type(self, new_graph_type):
        self.graph_type = new_graph_type
        self.update_info()

    def color_bind(self, canvas, color):
        canvas.tag_bind(color, '<1>', lambda e: self.set_color(color))

    def graph_type_bind(self, canvas, graph_type):
        canvas.tag_bind(graph_type, '<1>',
                        lambda e: self.set_graph_type(graph_type))

    def layout(self):
        self.selector.grid(row=0, column=0)
        self.info.grid(row=1, column=0)


if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    selector = SelectorFrame(root)
    selector.layout()
    selector.grid()
    root.mainloop()
