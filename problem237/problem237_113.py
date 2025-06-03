import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from operator import itemgetter

# 区間スケジューリング

N = int(readline())
m = map(int,read().split())
XL = zip(m,m)

LR = [(x-l,x+l) for x,l in XL]
LR.sort(key = itemgetter(1))

INF = 10 ** 18
prev_R = -INF
cnt = 0
for L,R in LR:
    if prev_R > L:
        continue
    cnt += 1
    prev_R = R

print(cnt)
