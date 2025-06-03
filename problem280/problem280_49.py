import itertools
import math

n = int(input())
l = []
for _ in range(n):
    x, y = map(int, input().split())
    l.append((x,y))

def d(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

ans = 0

for v in itertools.permutations(l):
    s = 0
    for i in range(n-1):
        s += d(v[i], v[i+1])
    ans += s

print(ans / math.factorial(n))