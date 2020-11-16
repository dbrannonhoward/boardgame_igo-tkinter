from CONSTANTS.COLORS import *
from CONSTANTS.DIMENSIONS import *
import tkinter as tk


class GameBoard:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=TOP, width=RIGHT, bg='gray')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.draw_board)
        self.calculate_square_size_for_game_space()

    def calculate_square_size_for_game_space(self):
        self.square_size = int(TOP / SPACE_SIZE)  # BW/SP is equally valid

    def assign_canvas_coordinates_to_discrete_game_tiles(self):
        tile_dict = dict()
        for tile in range(1, 10):
            for x_canvas_pixel in (BOTTOM, TOP):
                for y_canvas_pixel in (BOTTOM, TOP):
                    x_lower_bound = tile * self.square_size
                    if  < x_canvas_pixel <


    def draw_board(self, event=None):
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.canvas.delete('grid_line')
        for i in range(0, self.width, int(RIGHT / SPACE_SIZE)):
            self.canvas.create_line([(i, 0), (i, self.height)], tag='grid_line')

        for i in range(0, self.height, int(TOP / SPACE_SIZE)):
            self.canvas.create_line([(0, i), (self.width, i)], tag='grid_line')

    def draw_square_of_color(self, color):
        self.canvas.create_rectangle(self.x_lower_bound,
                                     self.y_lower_bound,
                                     self.x_upper_bound,
                                     self.y_upper_bound,
                                     fill=color)

    def draw_square_at(self, x_pos_selected, y_pos_selected) -> list:
        self.x_found, self.y_found = False, False
        x_pos_selected -= 1
        y_pos_selected -= 1
        try:
            for pos_lower_grid_line in range(BOTTOM, TOP, self.square_size):
                if pos_lower_grid_line == x_pos_selected * self.square_size:
                    self.x_lower_bound, self.x_upper_bound = \
                        pos_lower_grid_line, pos_lower_grid_line + self.square_size
                    self.x_found = True
                if pos_lower_grid_line == y_pos_selected * self.square_size:
                    self.y_lower_bound, self.y_upper_bound = \
                        pos_lower_grid_line, pos_lower_grid_line + self.square_size
                    self.y_found = True
                if self.x_found and self.y_found:
                    self.draw_square_of_color(SQUARE_COLOR)
        except ArithmeticError as BND_ERR:
            raise BND_ERR

    def main_loop(self):
        self.root.mainloop()

    def update(self):

        pass


if __name__ == '__main__':
    gb = GameBoard()
    gb.main_loop()
