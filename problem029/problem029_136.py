from math import sqrt, pow

x1, y1, x2, y2 = list(map(float, input().split()))
print(sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2)))

