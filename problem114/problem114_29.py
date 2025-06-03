import numpy as np

D = int(input())
c = np.array(list(map(int, input().split())))
s = np.array([list(map(int, input().split())) for x in range(D)])
t = np.array([int(input()) for x in range(D)])
last = np.zeros(26, dtype=np.int16)

score = 0
for d in range(1, D + 1):
    score += s[d - 1, t[d - 1] - 1]
    last[t[d - 1] - 1] = d
    score -= (c * (d - last)).sum()
    print(score)