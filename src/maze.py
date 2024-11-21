import time
import random
from src.cell import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win if win else None
        self.seed = random.seed(seed) if seed else None

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                cell_x1 = self.x1 + j * self.cell_size_x
                cell_y1 = self.y1 + i * self.cell_size_y
                cell_x2 = cell_x1 + self.cell_size_x
                cell_y2 = cell_y1 + self.cell_size_y

                cell = Cell(cell_x1, cell_y1, cell_x2, cell_y2, self.win)
                row.append(cell)

                self._draw_cell(cell)
            self._cells.append(row)

    def _draw_cell(self, cell):
        cell.draw()
        self._animate()

    def _animate(self):
        self.win.root.update()
        time.sleep(0.02)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0])
    
        last_row = len(self._cells) - 1
        last_col = len(self._cells[0]) - 1
        self._cells[last_row][last_col].has_bottom_wall = False
        self._draw_cell(self._cells[last_row][last_col])

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)
        for direction in directions:
            ni, nj = i + direction[0], j + direction[1]
            if 0 <= ni < self.num_rows and 0 <= nj < self.num_cols and not self._cells[ni][nj].visited:
                if direction == (0, -1):
                    self._cells[i][j].has_left_wall = False
                    self._cells[ni][nj].has_right_wall = False
                elif direction == (0, 1):
                    self._cells[i][j].has_right_wall = False
                    self._cells[ni][nj].has_left_wall = False
                elif direction == (-1, 0):
                    self._cells[i][j].has_top_wall = False
                    self._cells[ni][nj].has_bottom_wall = False
                elif direction == (1, 0):
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[ni][nj].has_top_wall = False

                self._break_walls_r(ni, nj)

        self._draw_cell(self._cells[i][j])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True

        self._cells[i][j].visited = True
        self._animate()
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < self.num_rows and 0 <= nj < self.num_cols:
                if not self._cells[i][j].has_bottom_wall and di == 1:
                    next_cell = self._cells[ni][nj]
                    if not next_cell.visited:
                        self._draw_line(i, j, ni, nj)
                        if self._solve_r(ni, nj):
                            return True
                        self._undo_move(i, j, ni, nj)

                elif not self._cells[i][j].has_top_wall and di == -1:
                    next_cell = self._cells[ni][nj]
                    if not next_cell.visited:
                        self._draw_line(i, j, ni, nj)
                        if self._solve_r(ni, nj):
                            return True
                        self._undo_move(i, j, ni, nj)

                elif not self._cells[i][j].has_right_wall and dj == 1:
                    next_cell = self._cells[ni][nj]
                    if not next_cell.visited:
                        self._draw_line(i, j, ni, nj)
                        if self._solve_r(ni, nj):
                            return True
                        self._undo_move(i, j, ni, nj)

                elif not self._cells[i][j].has_left_wall and dj == -1:
                    next_cell = self._cells[ni][nj]
                    if not next_cell.visited:
                        self._draw_line(i, j, ni, nj)
                        if self._solve_r(ni, nj):
                            return True
                        self._undo_move(i, j, ni, nj)

        return False

    def _draw_line(self, i, j, ni, nj):
        if self.win:
            self.win.canvas.create_line(
                (self.x1 + j * self.cell_size_x + self.cell_size_x / 2),
                (self.y1 + i * self.cell_size_y + self.cell_size_y / 2),
                (self.x1 + nj * self.cell_size_x + self.cell_size_x / 2),
                (self.y1 + ni * self.cell_size_y + self.cell_size_y / 2),
                fill="green", width=2
            )
        self._animate()

    def _undo_move(self, i, j, ni, nj):
        if self.win:
            self.win.canvas.create_line(
                (self.x1 + j * self.cell_size_x + self.cell_size_x / 2),
                (self.y1 + i * self.cell_size_y + self.cell_size_y / 2),
                (self.x1 + nj * self.cell_size_x + self.cell_size_x / 2),
                (self.y1 + ni * self.cell_size_y + self.cell_size_y / 2),
                fill="#808080", width=2
            )
        self._animate()
