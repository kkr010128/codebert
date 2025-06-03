from itertools import permutations
from math import sqrt, pow, factorial

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

def calc(a, b):
    [x1, y1] = a
    [x2, y2] = b
    return sqrt(pow(x1 - x2, 2) + pow(y1 -y2, 2))
ans = 0
for order in permutations(range(N)):
    tmp = 0
    for i in range(1, N):
        tmp += calc(l[order[i]], l[order[i-1]])
    ans += tmp
print(ans/factorial(N))


