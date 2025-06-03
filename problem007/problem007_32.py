n = int(raw_input())
dp = {}

def fib(n):
    if n in dp: return dp[n]
    if n == 0:
        dp[n] = 1
        return 1
    elif n == 1:
        dp[n] = 1
        return 1
    else:
        dp[n] = fib(n-1)+fib(n-2)
        return dp[n]

print fib(n)