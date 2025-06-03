import numpy as np

D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(D)]

I = [[0 for i in range(26)] for j in range(D)]

for d in range(D):
    for t in range(26):
        I[d][t] = (c[t] * (D-(d+1))) + s[d][t]

for line in I:
    print(line.index(max(line))+1)