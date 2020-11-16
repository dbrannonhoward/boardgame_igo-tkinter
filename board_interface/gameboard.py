from CONSTANTS.DIMENSIONS import *
import tkinter as tk


class GameBoard:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=BH, width=BW, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.draw_board)

    def draw_board(self, event=None):
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.canvas.delete('grid_line')
        for i in range(0, self.width, int(BW/SP)):
            self.canvas.create_line([(i, 0), (i, self.height)], tag='grid_line')

        for i in range(0, self.height, int(BH/SP)):
            self.canvas.create_line([(0, i), (self.width, i)], tag='grid_line')

    def main_loop(self):
        self.root.mainloop()

    def update(self):
        pass


if __name__ == '__main__':
    gb = GameBoard()
    gb.main_loop()
