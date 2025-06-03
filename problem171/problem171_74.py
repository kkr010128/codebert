import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))
from collections import defaultdict
def resolve():
    N = ir()
    A = sorted([[i+1, d] for i, d in enumerate(lr())], key=lambda x: x[1])[::-1]
    dp = defaultdict(lambda: -float('inf'))
    dp[0, 0] = 0
    for x in range(N):
        for y in range(N-x):
            i, d = A[x+y]
            dp[x+1, y] = max(dp[x, y]+d*(i-x-1), dp[x+1, y])
            dp[x, y+1] = max(dp[x, y]+d*(N-y-i), dp[x, y+1])
    ans = 0
    for i in range(N+1):
        ans = max(ans, dp[i, N-i])
    print(ans)
resolve()