#!python3

iim = lambda: map(int, input().rstrip().split())

def resolve():
    n, m = iim()
    C = list(iim())

    dp = [n] * (n + 1)
    dp[0] = 0
    for co in C:
        for i in range(co, n+1):
            dp[i] = min(dp[i], dp[i-co] + 1)
    print(dp[n])

if __name__ == "__main__":
    resolve()

