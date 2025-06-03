N = int(input())
dp = [None] * (N + 1)

def fib(n):
    if dp[n] != None:
        return dp[n]
    if n == 0 or n == 1:
        dp[n] = 1
    else:
        dp[n] = fib(n - 2) + fib(n - 1)
    return dp[n]

print(fib(N))
