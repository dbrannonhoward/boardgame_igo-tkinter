import tkinter as tk


class Application(tk.Frame):  # Application inherits tk.Frame
    def __init__(self, master=None):
        super().__init__(master)  # Uses tk.Frame init
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Hello World Button Creation
        self.hi_there = tk.Button(self)  # self.hi_there is a Button
        self.hi_there["text"] = "Hello World\n(click me)"  # Button attribute "text" sets display text
        self.hi_there["command"] = self.say_hi  # Button attribute "command" sets function call
        self.hi_there.pack(side="top")  # Button attribute side="top" does TODO Button.Pack() does what?
        # Quit Button Creation
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    # If I make this function @staticmethod it breaks stuff, TODO look into why
    def say_hi(self):  # Typical function definition
        print("hi there, everyone!")


root = tk.Tk()  # tk.Tk() is the main window TODO (I think??)
app = Application(master=root)  # app is an Application class object with master=tk.Tk()
app.mainloop()  # mainloop() keeps interface alive
