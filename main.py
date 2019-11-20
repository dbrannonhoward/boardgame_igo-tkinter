# import everything from tkinter module
from tkinter import *
#
master = Tk()
def callback():
    print("Printing to the terminal")
btn = Button(master, text="Print to the Terminal", command=callback)
btn.pack()
mainloop()

#end of file
