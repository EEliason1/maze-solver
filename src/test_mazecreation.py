import unittest
from unittest.mock import MagicMock
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        mock_win = MagicMock()
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, mock_win)
        
        self.assertEqual(len(m1._cells), num_rows)
        self.assertEqual(len(m1._cells[0]), num_cols)
    
    def test_maze_different_sizes(self):
        mock_win = MagicMock()
        m2 = Maze(0, 0, 5, 5, 15, 15, mock_win)
        self.assertEqual(len(m2._cells), 5)
        self.assertEqual(len(m2._cells[0]), 5)
        
        m3 = Maze(0, 0, 1, 1, 20, 20, mock_win)
        self.assertEqual(len(m3._cells), 1)
        self.assertEqual(len(m3._cells[0]), 1)

    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        mock_win = MagicMock()

        maze = Maze(0, 0, num_rows, num_cols, 20, 20, mock_win)

        self.assertFalse(maze._cells[0][0].has_top_wall)
        self.assertFalse(maze._cells[num_rows - 1][num_cols - 1].has_bottom_wall)

if __name__ == "__main__":
    unittest.main()