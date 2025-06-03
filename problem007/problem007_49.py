

def fibonacciDP(i):
    if i == 0:
        return 1
    elif i == 1:
        return 1
    else:
        if dp[i-1] is None and dp[i-2] is None:
            dp[i-1] = fibonacciDP(i-1)
            dp[i-2] = fibonacciDP(i-2)
        elif dp[i-1] is None:
            dp[i-1] = fibonacciDP(i-1)
        elif dp[i-2] is None:
            dp[i-2] = fibonacciDP(i-2)

        return dp[i-1]+ dp[i-2]

def fibonacci(i):
    if i == 0:
        return 1
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1)+fibonacci(i-2)



n = int(input())
dp = [None]*n

print(fibonacciDP(n))