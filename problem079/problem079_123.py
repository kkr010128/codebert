import sys
sys.setrecursionlimit(100000000)
S = int(input())

mod = 10**9+7

def dfs_memo(n):
    memo = [0]*(n+1)
    memo[3] = 1

    def dfs(n):
        if n < 3:
            return 0
        elif memo[n] != 0:
            return memo[n]
        memo[n] = dfs(n-1)+dfs(n-3)
        return memo[n]
    return dfs(n)

if S <3:
    print(0)
else:
    print(dfs_memo(S)%mod)