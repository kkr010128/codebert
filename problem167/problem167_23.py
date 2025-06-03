import math
r = int(input())
x = r * math.pi * 2
n = 10
y = math.floor(x * 10 ** n) / (10 ** n)
print(y)
