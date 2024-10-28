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

if __name__ == "__main__":
    unittest.main()