import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    c = list(map(int, input().split()))

    dp = [i+100 for i in range(N+1)]
    dp[0] = 0

    for i in range(1, N+1):
        for t in c:
            if i - t >= 0:
                dp[i] = min(dp[i], dp[i-t] + 1)
    # print(dp)
    print(dp[N])

if __name__ == "__main__":
    main()
