from tkinter import *

master = Tk()

canvas_var = Canvas(master, width=646, height=646)
canvas_var.pack()

canvas_var.create_line(0, 0, 200, 100)
canvas_var.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

canvas_var.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()