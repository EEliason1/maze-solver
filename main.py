from src.window import Window
from src.point import Point
from src.line import Line
from src.cell import Cell
from src.maze import Maze

def main():
    win = Window(800, 800)

    maze = Maze(50, 50, 15, 15, 40, 40, win)
    maze.solve()

    win.wait_for_close()

main()