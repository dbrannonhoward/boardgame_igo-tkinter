# reference code from https://stackoverflow.com/questions/34006302/how-to-create-a-grid-on-tkinter-in-python
import tkinter as tkinter


def create_grid(event=None):
    width_of_canvas = canvas.winfo_width()  # Get current width of canvas
    height_of_canvas = canvas.winfo_height()  # Get current height of canvas
    canvas.delete('grid_line')  # Will only remove the grid_line

    # With arbitrary game board size 646x646, use 34 pixels to achieve a 19x19 grid
    for i in range(0, width_of_canvas, 34):  # range(start, stop, step)
        canvas.create_line([(i, 0), (i, height_of_canvas)], tag='grid_line')

    # With arbitrary game board size 646x646, use 34 pixels to achieve a 19x19 grid
    for i in range(0, height_of_canvas, 34):
        canvas.create_line([(0, i), (width_of_canvas, i)], tag='grid_line')


master = tkinter.Tk()
canvas = tkinter.Canvas(master, height=646, width=646, bg='white')
canvas.pack(fill=tkinter.BOTH, expand=True)
canvas.bind('<Configure>', create_grid)
master.mainloop()
