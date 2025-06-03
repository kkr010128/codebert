import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

X, N = mapint()
A = set(range(1000))
Ps = list(mapint())
Ps = sorted(list(A-set(Ps)))
mi = 10**18
ans = 0
for p in Ps:
    if abs(X-p)<mi:
        ans = p
        mi = abs(X-p)

print(ans)