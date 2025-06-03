num = int(input())

dp = { 0: 1, 1: 1 }
def fibonacci(n):
  if not n in dp:
    dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
  return dp[n]

print(fibonacci(num))

