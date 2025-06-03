# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(H, N, AB):
    INF = 10**9
    dp = [INF] * (H + 1)
    dp[H] = 0
    for h in reversed(range(H + 1)):
        for i, (a, b) in enumerate(AB):
            nh = max(0, h - a)
            dp[nh] = min(dp[nh], dp[h] + b)
    print(dp[0])

if __name__ == '__main__':
    input = sys.stdin.readline
    H, N = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    main(H, N, AB)
