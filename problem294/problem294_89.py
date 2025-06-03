import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Ls = list(mapint())
Ls.sort()

from bisect import bisect_left
ans = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        idx = bisect_left(Ls, Ls[i]+Ls[j])
        ans += idx-1-j

print(ans)