from shapes import Line, Point
from window import Window

class Cell:

    def __init__(self, x1, y1, x2, y2, window : Window):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
    def draw(self):
        top_right = Point(self._x2, self._y1)
        bottom_right = Point(self._x2, self._y2)
        bottom_left = Point(self._x1, self._y2)
        top_left = Point(self._x1, self._y1)
        if self.has_left_wall:
            self._window.draw_line(Line(top_left, bottom_left), "black")
        if self.has_right_wall:
            self._window.draw_line(Line(top_right, bottom_right), "black")
        if self.has_top_wall:
            self._window.draw_line(Line(top_left, top_right), "black")
        if self.has_bottom_wall:
            self._window.draw_line(Line(bottom_right, bottom_left), "black")