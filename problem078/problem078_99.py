MOD = 10**9+7
def solve(n):
    """
    0: {}
    1: {0}
    2: {9}
    3: {0,9}
    """
    dp = [[0]*4 for i in range(n+1)]
    dp[0][0] = 1
    x = [1,0,0,0]
    for i in range(n):
        x = [
            (8*x[0]) % MOD,
            (9*x[1] + x[0]) % MOD,
            (9*x[2] + x[0]) % MOD,
            (10*x[3] + x[2] + x[1]) % MOD
        ]
    return x[3]

n = int(input())
print(solve(n))