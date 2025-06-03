import sys
input = sys.stdin.readline
def main():
    S = int(input())
    dp = [0]*(S+1)
    dp[0] = 1
    M = 10**9 + 7
    for i in range(1, S+1):
        for j in range(0,i-2):
            dp[i] += dp[j]
            dp[i] %= M
    print(dp[S])

if __name__ == '__main__':
    main()