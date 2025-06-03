from collections import defaultdict
iim = lambda: map(int, input().rstrip().split())
 
def resolve():
    N = int(input())
    A = list(iim())
    ans = 0
    dp = [0]*N
    for i, ai in enumerate(A):
        x = i + ai
        if x < N:
            dp[x] += 1
        x = i - ai
        if x >= 0:
            ans += dp[x]
    print(ans)
resolve()