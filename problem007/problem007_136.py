# -*- coding:utf-8 -*-

def solve():
    import sys

    N = int(sys.stdin.readline())

    dp = [None]*45
    dp[0], dp[1] = 1, 1

    def fib(n):
        if dp[n] is not None:
            return dp[n]
        dp[n] = fib(n-1) + fib(n-2)
        return dp[n]

    print(fib(N))


if __name__ == "__main__":
    solve()

