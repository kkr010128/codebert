import sys


inint = lambda: int(sys.stdin.readline())
inintm = lambda: map(int, sys.stdin.readline().split())
inintl = lambda: list(inintm())
instrm = lambda: map(str, sys.stdin.readline().split())
instrl = lambda: list(instrm())

n = inint()
A = inintl()

cnt = 1
ans = 0

for a in A:
    if a != cnt:
        ans += 1
        continue
    else:
        cnt += 1

if cnt == 1:
    if ans == 0:
        print(ans)
    else:
        print(-1)
else:
    print(ans)
