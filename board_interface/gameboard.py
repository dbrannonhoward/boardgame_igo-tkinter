from CONSTANTS.COLORS import *
from CONSTANTS.DIMENSIONS import *
from random import randint
import tkinter as tk


class GameBoard:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=TOP, width=RIGHT, bg='gray')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.draw_board)
        self.calculate_tile_size_relative_to_board_size()
        self.generate_semi_random_patterns()

    def calculate_tile_size_relative_to_board_size(self):
        self.tile_size = int(TOP / TILE_SIZE)  # BW/SP is equally valid

    def draw_board(self, event=None):
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.canvas.delete('grid_line')
        for i in range(0, self.width, int(RIGHT / TILE_SIZE)):
            self.canvas.create_line([(i, 0), (i, self.height)], tag='grid_line')

        for i in range(0, self.height, int(TOP / TILE_SIZE)):
            self.canvas.create_line([(0, i), (self.width, i)], tag='grid_line')

    def draw_shape_of_color(self, shape, color):
        if shape == "oval":
            self.canvas.create_oval(self.x_lower_bound,
                                    self.y_lower_bound,
                                    self.x_upper_bound,
                                    self.y_upper_bound,
                                    fill=color)
        elif shape == "square":
            self.canvas.create_rectangle(self.x_lower_bound,
                                         self.y_lower_bound,
                                         self.x_upper_bound,
                                         self.y_upper_bound,
                                         fill=color)
        else:
            raise RuntimeError

    def draw_shape_at(self, shape, x_pos_selected, y_pos_selected) -> list:
        self.x_found, self.y_found = False, False
        x_pos_selected -= 1
        y_pos_selected -= 1
        try:
            for pos_lower_grid_line in range(BOTTOM, TOP, self.tile_size):
                if pos_lower_grid_line == x_pos_selected * self.tile_size:
                    self.x_lower_bound, self.x_upper_bound = \
                        pos_lower_grid_line, pos_lower_grid_line + self.tile_size
                    self.x_found = True
                if pos_lower_grid_line == y_pos_selected * self.tile_size:
                    self.y_lower_bound, self.y_upper_bound = \
                        pos_lower_grid_line, pos_lower_grid_line + self.tile_size
                    self.y_found = True
                if self.x_found and self.y_found:
                        self.draw_shape_of_color(shape, SHAPE_COLOR)
        except ArithmeticError as BND_ERR:
            raise BND_ERR

    def draw_square_at_mouse_tile(self):
        pass

    def generate_semi_random_patterns(self):
        self.canvas.delete('ALL')
        for x in range(20):
            for y in range(20):
                if x % randint(1, 19) == 0 or y % randint(1, 19) == 0:
                    self.draw_shape_at("oval", x, y)
                else:
                    self.draw_shape_at("square", x, y)
        self.root.after(1000, self.generate_semi_random_patterns())

    def main_loop(self):
        self.root.mainloop()


if __name__ == '__main__':
    gb = GameBoard()
    gb.main_loop()
