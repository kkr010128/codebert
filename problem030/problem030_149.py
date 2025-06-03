import math

class Triangle():

    def __init__(self, edge1, edge2, angle):
        self.edge1 = edge1
        self.edge2 = edge2
        self.angle = angle
        self.edge3 = math.sqrt(edge1 ** 2 + edge2 ** 2 - 2 * edge1 * edge2 * math.cos(math.radians(angle)))
        self.height = edge2 * math.sin(math.radians(angle))
        self.area = edge1 * self.height / 2

a, b, theta = [int(i) for i in input().split()]

triangle = Triangle(a, b, theta)

print(triangle.area)
print(triangle.edge1 + triangle.edge2 + triangle.edge3)
print(triangle.height)
