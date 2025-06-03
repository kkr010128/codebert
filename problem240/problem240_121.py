import collections

N, M = map(int, input().split())
WA_CNT = {}
CLEAR = {}
for i in range(M):
    P, S = input().split()
    if P in CLEAR:
        continue
    if S == "AC":
        CLEAR[P] = 1
        continue

    if not P in WA_CNT:
        WA_CNT[P] = 0
    WA_CNT[P] += 1


num = len(CLEAR)
try_num = 0
for i in CLEAR:
    if i in WA_CNT:
        try_num += WA_CNT[i]
print("{} {}".format(num, try_num))