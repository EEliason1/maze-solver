class Cell():
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        self._win = win if win else None

    def draw(self):
        if self._win:
            if self.has_top_wall:
                self._win.canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill="black", width=2)
            else:
                self._win.canvas.create_line(self._x1, self._y1, self._x2, self._y1, fill="#d9d9d9", width=2)  # background color
            
            if self.has_bottom_wall:
                self._win.canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill="black", width=2)
            else:
                self._win.canvas.create_line(self._x1, self._y2, self._x2, self._y2, fill="#d9d9d9", width=2)
                
            if self.has_left_wall:
                self._win.canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill="black", width=2)
            else:
                self._win.canvas.create_line(self._x1, self._y1, self._x1, self._y2, fill="#d9d9d9", width=2)
                
            if self.has_right_wall:
                self._win.canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill="black", width=2)
            else:
                self._win.canvas.create_line(self._x2, self._y1, self._x2, self._y2, fill="#d9d9d9", width=2)

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"

        x1_center = (self._x1 + self._x2) // 2
        y1_center = (self._y1 + self._y2) // 2
        x2_center = (to_cell._x1 + to_cell._x2) // 2
        y2_center = (to_cell._y1 + to_cell._y2) // 2

        self._win.canvas.create_line(
            x1_center, y1_center, x2_center, y2_center, fill=color, width=2
        )
