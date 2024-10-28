class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y
        
class Line:
    def __init__(self, p1 : Point, p2 : Point):
        self.p1 = p1
        self.p2 = p2
        
    def draw(self, canvas, fill_color):
        canvas.create_line(*self.p1, *self.p2, fill=fill_color, width=2)
        