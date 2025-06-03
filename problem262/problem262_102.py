import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
XY = []
for _ in range(N):
    A = int(input())
    xy = [list(mapint()) for _ in range(A)]
    XY.append(xy)

ans = 0
for i in range(1<<N):
    honest = [-1]*N
    cnt = 0
    ok = True
    for j in range(N):
        if (i>>j)&1:
            honest[j]=1
        else:
            honest[j]=0
    for j in range(N):
        if (i>>j)&1:
            cnt += 1
            for x, y in XY[j]:
                if honest[x-1]!=y:
                    ok = False
                    break
    if ok:
        ans = max(ans, cnt)

print(ans)
