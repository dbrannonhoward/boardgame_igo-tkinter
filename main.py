from tkinter import *

root = Tk()

# some canvas testing

c = Canvas(root, height=500, width=500)
c.pack()

for step_size in range(15, 90, 15):
    for i in range(5, 500, step_size):
        if i % 2 == 0:
            c.create_oval(i, i, i+step_size, i+step_size, fill="black", outline="white")
        else:
            c.create_oval(i, i, i+step_size, i+step_size, fill="white", outline="black")

mainloop()