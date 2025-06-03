import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
P = inintl()

min_l = []
now_min = P[0]
ans = 0

for p in P:
    if p < now_min:
        now_min = p
    min_l.append(now_min)

for i in range(n):
    if min_l[i] == P[i]:
        ans += 1

print(ans)
