#บวกสี่เหลี่ยมสองอัน โดยนำความกว้างสองอันบวกกัน และนำความสูงที่ยาวที่สุดในสองอันมาเป็นความสูงของสี่เหลี่ยมผลลัพธ์

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):
        return Point(self.x * scalar)
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    

class Rectangle(Point):
    def __init__(self,x1,x2,y1,y2):
        self.w = x2 - x1
        self.h = y1 - y2
    
    def __add__(self, other):
        new_w = self.w + other.w
        new_h = max(self.h, other.h)
        return Rectangle(0, new_w, new_h, 0)
    
    def __str__(self):
        return f"Rectangle(width = {self.w}, height = {self.h})"
    
r1 = Rectangle(1,2,1,-1)
r2 = Rectangle(2, 4, 2, 0)
r3 = r1 + r2

print(r3)

