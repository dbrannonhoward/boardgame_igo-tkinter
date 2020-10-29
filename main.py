import tkinter as tk


class ButtonBoard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # buttons
        self.top_left = tk.Button(self)
        self.top_right = tk.Button(self)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        # pack
        self.pack()
        self.create_buttons()

    def create_buttons(self):
        self.top_left["text"] = "top left"
        self.top_right["text"] = "top right"

        self.top_left["command"] = self.top_left_button
        self.top_right["command"] = self.top_right_button

        self.top_left.pack(side="left")
        self.top_right.pack(side="right")
        self.quit.pack(side="bottom")

    def top_left_button(self):
        print("top left button")

    def top_right_button(self):
        print("top right button")


if __name__ == '__main__':
    root = tk.Tk()
    app = ButtonBoard(master=root)
    app.mainloop()
