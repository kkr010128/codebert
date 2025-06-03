import sys
import math

a = []
for l in sys.stdin:
    a.append(int(l))

h = a[0]
n = 0
while h > 1:
    h = math.floor(h / 2)
    n = n + 1 

print(2 ** (n + 1) - 1)