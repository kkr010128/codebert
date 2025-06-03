from itertools import permutations
from math import factorial
N = int(input())
data = []
for _ in range(N):
    x, y = map(int, input().split())
    data.append((x,y))
res = 0
for a in permutations(data,N):
    x0, y0 = a[0]
    for x, y in a[1:]:
        res += ((x-x0)**2 + (y-y0)**2)**(0.5)
        x0, y0 = x, y

print(res/factorial(N))