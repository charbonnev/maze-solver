from window import Window
from shapes import Line, Point
from cell import Cell

draw_some_lines = False
draw_some_cells = True

def main():
    win = Window(800,600)
    
    c_w = 50
    c_h = 50
    
    if draw_some_cells:
        cell = Cell(50, 50, 150, 150, win)
        cell.has_bottom_wall = True
        cell.has_right_wall  = True
        cell.has_top_wall    = True
        cell.has_left_wall   = True
        cell.draw()
        cell = Cell(100, 100, 200, 200, win)
        cell.has_bottom_wall = True
        cell.has_right_wall  = False
        cell.has_top_wall    = True
        cell.has_left_wall   = True
        cell.draw()
        cell = Cell(200, 200, 300, 300, win)
        cell.has_bottom_wall = True
        cell.has_right_wall  = True
        cell.has_top_wall    = False
        cell.has_left_wall   = False
        cell.draw()
        cell = Cell(300, 300, 400, 400, win)
        cell.has_bottom_wall = False
        cell.has_right_wall  = False
        cell.has_top_wall    = True
        cell.has_left_wall   = True
        cell.draw()
        cell = Cell(400, 400, 500, 500, win)
        cell.has_bottom_wall = True
        cell.has_right_wall  = False
        cell.has_top_wall    = False
        cell.has_left_wall   = True
        cell.draw()
        cell = Cell(500, 500, 600, 600, win)
        cell.has_bottom_wall = False
        cell.has_right_wall  = True
        cell.has_top_wall    = True
        cell.has_left_wall   = False
        cell.draw()
    
    if draw_some_lines:
        win.draw_line(Line(Point(0, 0), Point(100, 200)), "red")
        win.draw_line(Line(Point(200, 0), Point(0, 300)), "green")
        win.draw_line(Line(Point(0, 150), Point(800, 0)), "blue")
        win.draw_line(Line(Point(500, 600), Point(0, 0)), "yellow")    
    win.wait_for_close()
    
main()