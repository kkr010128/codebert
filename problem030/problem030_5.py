import math
a,b,C = map(float,input().split())
C = math.pi* C / 180
area = (a * b  * math.sin(C) / 2)
print(area)
print(a + b + math.sqrt(a**2 + b**2 - 2 * a * b* math.cos(C)))
print(area * 2 / a)