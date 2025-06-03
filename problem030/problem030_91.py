from math import sqrt, radians, sin, cos

class Triangle (object):
    def __init__(self, a, b, C):
        self.a = a
        self.b = b
        self.C = radians(C)

    def getArea(self):
        return self.a * self.getHeight() / 2

    def getPerimeter(self):
        return self.a + self.b + sqrt(self.a ** 2 - 2 * self.a * self.b * cos(self.C) + self.b ** 2)

    def getHeight(self):
        return self.b * sin(self.C)

tri = Triangle(*[int(e) for e in input().split()])
print(tri.getArea())
print(tri.getPerimeter())
print(tri.getHeight())

    
