# Triangle

from math import *

triangle = [int(i) for i in input().rstrip().split()]
sides = [triangle[0], triangle[1]]
a = sides[0]
b = sides[1]
angle = triangle[2]

triangleArea = 0.5 * a * b * sin(radians(angle))
print(triangleArea)

otherSideSquare = a ** 2 + b ** 2 - 2 * a * b * cos(radians(angle))
otherSide = otherSideSquare ** 0.5
circumference = a + b + otherSide
print(circumference)

height = triangleArea / 0.5 / a
print(height)

