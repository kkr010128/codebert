import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
es = []
for _ in range(N):
    x, l = mapint()
    es.append((x+l, x-l))

es.sort()
now = -10**18
idx = 0
ans = 0
while 1:
    if idx==N:
        break
    end, start = es[idx]
    if start>=now:
        now = end
        ans += 1
    idx += 1

print(ans)