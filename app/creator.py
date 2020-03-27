'''Use help reference at https://www.jianshu.com/p/c6a2b400d0b9
'''
from tkinter import ttk

from atom import Meta
from param import Param


class SelectorMeta(Meta):
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
        for k, color in enumerate(SelectorMeta.colors):
            t = 7+30*(k+1)
            direction = self.start+t, self.start-20, self.end+t, self.end-20
            self.draw_graph('rectangle', direction,
                            'yellow', tags=color, fill=color)
        self.dtag('rectangle')

    def create_shape(self):
        '''Set the shape selector'''
        self.create_text((self.start-10, self.start+30),
                         text='shape', font='Times 15', anchor='w')
        for k, shape in enumerate(SelectorMeta.shapes):
            t = 7+30*(k+1)
            direction = self.start+t, self.start+20, self.end+t, self.end+20
            width = 10 if shape == 'line' else 1
            fill = 'blue' if 'point' in shape else 'white'
            self.draw_graph(shape.split(
                '_')[0], direction, 'blue', width=width, tags=shape, fill=fill)


class _SelectBind:
    # 初始化参数
    color = Param()
    graph_type = Param()

    def __init__(self, selector, graph_type=None, color=None):
        '''The base class of all graphics frames.

        :param selector: a instance of Selector.
        '''
        self.color = color
        self.graph_type = graph_type
        [self.color_bind(selector, color) for color in selector.colors]
        [self.graph_type_bind(selector, graph_type)
         for graph_type in selector.shapes]
        selector.dtag('all')

    def set_color(self, new_color):
        self.color = new_color
        print(self.color)

    def set_graph_type(self, new_graph_type):
        self.graph_type = new_graph_type

    def color_bind(self, canvas, color):
        canvas.tag_bind(color, '<1>', lambda e: self.set_color(color))

    def graph_type_bind(self, canvas, graph_type):
        canvas.tag_bind(graph_type, '<1>',
                        lambda e: self.set_graph_type(graph_type))

class Selector(ttk.Frame):
    def __init__(self, master=None, **kw):
        '''The base class of all graphics frames.

        :param master: a widget of tkinter or tkinter.ttk.
        '''
        super().__init__(master, **kw)
        self.selector = Selector(self, background='lightgreen')


if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    selector = Selector(root, background='lightgreen')
    selector.grid()
    root.mainloop()
