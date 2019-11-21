from tkinter import *

root = Tk()
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

frame = Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

for row_index in range(19):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(19):
        Grid.columnconfigure(frame, col_index, weight=1)
        btn = Button(frame)
        btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)

root.mainloop()
