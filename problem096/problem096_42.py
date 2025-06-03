import math
n, d = map(int,input().split( ))
#print(n,d)
number = 0
for a in range(n):
    x, y = map(int, input().split( ))
    if math.sqrt(x**2 + y**2) <= d:
        number += 1
print(number)
