from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
pos = []
zero = []
neg = []
for _ in range(N):
    S = input().rstrip()
    m = s = 0
    for c in S:
        if c == '(':
            s += 1
        else:
            s -= 1
            m = min(m, s)
    if s > 0:
        heappush(pos, (-m, s)) # take larger mins first
    elif s == 0:
        heappush(zero, (m, s))
    else:
        heappush(neg, (m - s, s)) # take smaller mins first
num = 0
while pos:
    m, s = heappop(pos)
    if num - m < 0:
        print('No')
        exit()
    num += s
while zero:
    m, s = heappop(zero)
    if num + m < 0:
        print('No')
        exit()
while neg:
    m, s = heappop(neg)
    m += s
    if num + m < 0:
        print('No')
        exit()
    num += s
if num == 0:
    print('Yes')
else:
    print('No')

