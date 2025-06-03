MOD = 10 ** 9 + 7
INF = 10 ** 11
import sys
sys.setrecursionlimit(100000000)

N = int(input())
ans = []
def dfs(i,standard):
    if i == N:
        ans.append(standard)
        return
    before_M = max(ord(s) for s in standard)
    for j in range(97,before_M + 2):
        dfs(i + 1,standard + chr(j))
dfs(1,'a')
print('\n'.join(ans))
