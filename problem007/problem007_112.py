n = int(input())

def fib(n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1

    def fib_sub(n):
        if dp[n] != 0:
            return dp[n]

        fibn1 = fib_sub(n-1)
        fibn2 = fib_sub(n-2)
        dp[n-1] = fibn1
        dp[n-2] = fibn2
        return fibn1 + fibn2

    return fib_sub(n)
print(fib(n))

