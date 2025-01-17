class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.color +'+'+ other.color)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.color +'-'+ other.color)
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y, self.color +'*'+ other.color)
    def __str__(self):
        return f"Point({self.x}, {self.y}, {self.color})"
    
p1 = Point(2,3,"red")
p2 = Point(4,5,"Blue")

print(f"p1 + p2 = {p1+p2}")
print(f"p1 - p2 = {p1-p2}")
print(f"p1 - p2 = {p1*p2}")

