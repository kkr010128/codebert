import sys
from collections import defaultdict

N, M = map(int, input().split())

is_ac = [False] * N
wa = [0] * N

for i in range(M):
    p, S = input().split()
    n = int(p) - 1
    if not is_ac[n] and S == "AC":
        is_ac[n] = True
    if not is_ac[n] and S == "WA":
        wa[n] += 1

cnt_ac = is_ac.count(True)
cnt_wa = 0
for i in range(N):
    if is_ac[i]:
        cnt_wa += wa[i]
print(cnt_ac, cnt_wa)
