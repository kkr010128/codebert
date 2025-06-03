import sys
input = sys.stdin.readline

n = int(input())

plus = []
minus = []
for _ in range(n):
    min_s = 0
    ts = 0
    s = input().strip()
    for c in s:
        ts += 1 if c == '(' else -1
        min_s = min(ts, min_s)
    if ts >= 0:
        plus.append((-min_s, ts))
    else:
        minus.append((-(min_s - ts), -ts))

plus.sort()
minus.sort()

s1 = 0
for m, t in plus:
    if s1 - m < 0:
        print('No')
        exit()
    s1 += t

s2 = 0
for m, t in minus:
    if s2 - m < 0:
        print('No')
        exit()
    s2 += t

if s1 == s2:
    print('Yes')
else:
    print('No')
