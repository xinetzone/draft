from tkinter import Tk
from atom import Meta

if __name__ == "__main__":
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    self = Meta(root)
    kw = {
        'color': 'purple',
        'dash': 2,
        'width': 2,
        'tags': 'test '
    }
    name = 'oval'
    color = 'purple'
    width = 2
    self.draw_graph('line', [20, 20, 100, 200], **kw)
    self.draw_graph('oval', [50, 80, 100, 200], fill='red', **kw)
    self.draw_graph('rectangle', [170, 80, 220, 200], fill='yellow', **kw)
    self.draw_graph('arc', [180, 100, 250, 260],
                    fill='lightblue', style='chord', **kw)
    self.layout(row=0, column=0)
    print(self.gettags(1))
    print(self.find_withtag('graph'))
    root.mainloop()
