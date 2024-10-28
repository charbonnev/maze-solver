from tkinter import Tk, BOTH, Canvas
from shapes import Point, Line

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.configure(bg="white")
        self.canvas = Canvas(self.__root, width=width, height=height, background="white")
        self.canvas.pack()
        self.is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
            
    def close(self):
        self.is_running = False
        
    def draw_line(self, line: Line, fill_color):
        line.draw(self.canvas, fill_color)