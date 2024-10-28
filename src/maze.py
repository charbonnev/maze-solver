import time
from cell import Cell
from window import Window

class Maze:
    def __init__(self, x1, y1, num_rows : int, num_cols : int, cell_size_x, cell_size_y, window : Window = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._init_cells(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window)
        self._walls = []
        self._visited = [[False for j in range(num_cols)] for i in range(num_rows)]

    def _init_cells(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window):
        self._cells : list[list[Cell]] = []
        for i in range(num_cols):
            row = []
            for j in range(num_rows):
                x2 = x1 + (i + 1) * cell_size_x
                y2 = y1 + (j + 1) * cell_size_y
                cell = Cell(x1 + i * cell_size_x, y1 + j * cell_size_y, x2, y2, window)
                row.append(cell)
            self._cells.append(row)
            
    def _draw_cells(self):
        for row in self._cells:
            for cell in row:
                cell.draw()
                
    def _animate(self):
        self._window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].draw()