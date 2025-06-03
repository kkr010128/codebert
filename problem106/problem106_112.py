N = int(input())
from collections import Counter
c = Counter()
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            n = x*x + y*y + z*z + x*y + y*z + z*x
            c[n] += 1
for i in range(1,N+1):
    print(c[i])