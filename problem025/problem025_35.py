n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

"""
def exhaustive_search(m, i):
    if i == n:
        return 0
    if m < 0:
        return 0
    if m == A[i]:
        return 1
    return max(exhaustive_search(m, i + 1), exhaustive_search(m - A[i], i + 1))
"""

def dp_search(m):
    dp = [[1] + [0] * m for _ in range(n + 1)] # dp[i][j] i番目まででjを作れるか
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j >= A[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - A[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][m]

for mi in m:
    if dp_search(mi):
        print("yes")
    else:
        print("no")
