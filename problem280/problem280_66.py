from itertools import permutations as P
from math import sqrt as r

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
ans_sum = 0
town = list(P(list(range(N)), N))
Q = len(town)

for town in town:
    d = 0
    for i in range(N - 1):
        X = xy[town[i]][0] - xy[town[i + 1]][0]
        Y = xy[town[i]][1] - xy[town[i + 1]][1]
        d += r(X**2 + Y**2)
    #print(d)
    ans_sum += d

print(ans_sum/Q)