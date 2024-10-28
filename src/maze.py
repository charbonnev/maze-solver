import time
from cell import Cell
from window import Window
import random as r
from shapes import Line, Point


class Maze:
    def __init__(self, x1, y1, num_rows: int, num_cols: int, cell_size_x, cell_size_y, window: Window = None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window
        self._init_cells(x1, y1, num_rows, num_cols,
                         cell_size_x, cell_size_y, window)
        if seed:
            r.seed(seed)
        else:
            r.seed(0)

    def _init_cells(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window):
        self._cells: list[list[Cell]] = []
        for i in range(num_cols):
            row = []
            for j in range(num_rows):
                x2 = x1 + (i + 1) * cell_size_x
                y2 = y1 + (j + 1) * cell_size_y
                cell = Cell(x1 + i * cell_size_x, y1 +
                            j * cell_size_y, x2, y2, window)
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
        self._cells[self._num_cols - 1][self._num_rows -
                                        1].has_bottom_wall = False
        self._cells[self._num_cols - 1][self._num_rows - 1].draw()

    def _break_walls(self):
        self._break_walls_r(0, 0)
        self._reset_visited_cells()
        
    def _reset_visited_cells(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _break_walls_r(self, i: int, j: int):
        self._cells[i][j].visited = True
        while True:
            possible_directions : list[tuple[int, int]] = []
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append((i-1, j))
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                possible_directions.append((i+1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i, j-1))
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                possible_directions.append((i, j+1))
            if len(possible_directions) == 0:
                self._cells[i][j].draw()
                return
            else:
                (new_i, new_j) = r.choice(possible_directions)
                if new_i == i:
                    if new_j > j:
                        self._cells[i][j].has_bottom_wall = False
                        self._cells[new_i][new_j].has_top_wall = False
                    else:
                        self._cells[i][j].has_top_wall = False
                        self._cells[new_i][new_j].has_bottom_wall = False
                else:
                    if new_i < i:
                        self._cells[i][j].has_left_wall = False
                        self._cells[new_i][new_j].has_right_wall = False
                    else:
                        self._cells[i][j].has_right_wall = False
                        self._cells[new_i][new_j].has_left_wall = False
                self._cells[i][j].draw()
                self._break_walls_r(new_i, new_j)
                
    def _solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i: int, j: int):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if i + di < 0 or i + di >= self._num_cols or j + dj < 0 or j + dj >= self._num_rows:
                continue # out of bounds, try next direction
            if self._cells[i][j].has_left_wall and di == -1:
                continue # there's a left wall blocking us
            if self._cells[i][j].has_right_wall and di == 1:
                continue # there's a right wall blocking us
            if self._cells[i][j].has_top_wall and dj == -1:
                continue # there's a top wall blocking us
            if self._cells[i][j].has_bottom_wall and dj == 1:
                continue # there's a bottom wall blocking us
            if self._cells[i + di][j + dj].visited:
                continue # we've been here before, try next direction
            self._cells[i][j].draw_move(self._cells[i + di][j + dj])
            if self._solve_r(i + di, j + dj):
                return True
            self._cells[i][j].draw_move(self._cells[i + di][j + dj], undo=True)
        return False
        
