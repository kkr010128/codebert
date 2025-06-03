d = int(input())
cs = list(map(int, input().split()))
sm = [list(map(int, input().split())) for _ in range(d)]

import random
for i in range(d):
    mx = max(sm[i])
    t = sm[i].index(mx) + 1
    print(t)
