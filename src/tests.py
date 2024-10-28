import unittest
from maze import Maze
from cell import Cell

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        
    def test_maze_create_cells2(self):
        num_cols = 16
        num_rows = 9
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        cell = m2._cells[0][0]
        self.assertEqual(cell._x1, 0)
        self.assertEqual(cell._y1, 0)
        self.assertEqual(cell._x2, 10)
        self.assertEqual(cell._y2, 10)
        self.assertEqual(
            len(m2._cells),
            num_cols,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows,
        )
    
    def test_break_entrance_and_exit(self):
        num_cols = 16
        num_rows = 9
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m3._break_entrance_and_exit()
        entrance = m3._cells[0][0]
        exit = m3._cells[num_cols - 1][num_rows - 1]
        self.assertEqual(entrance.has_top_wall, False)
        self.assertEqual(exit.has_bottom_wall, False)
        
    def test_break_walls(self):
        num_cols = 16
        num_rows = 9
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m4._break_entrance_and_exit()
        m4._break_walls()
        entrance = m4._cells[0][0]
        exit = m4._cells[num_cols - 1][num_rows - 1]
        self.assertEqual(entrance.has_top_wall, False)
        self.assertEqual(exit.has_bottom_wall, False)
        self.assertEqual(entrance.visited, False)

if __name__ == "__main__":
    unittest.main()