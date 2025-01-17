#บวกสี่เหลี่ยมสองอัน โดยนำความกว้างสองอันบวกกัน และนำความสูงที่ยาวที่สุดในสองอันมาเป็นความสูงของสี่เหลี่ยมผลลัพธ์

class Rectangle:
    def __init__(self,x1,x2,y1,y2):
        self.w = x2 - x1
        self.h = y1 - y2
    
    def __add__(self, other):
        new_w = self.w + other.w
        new_h = max(self.h, other.h)
        return Rectangle(0, new_w, new_h, 0)
    
    def __str__(self):
        return f"New Rectangle width = {self.w}, height = {self.h}"
    
r1 = Rectangle(1,2,1,-1)
r2 = Rectangle(2, 4, 2, 0)
r3 = r1 + r2
print(r3)

