# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
def main(N, T, AB):
    dpL = [[0] * (T + 1) for _ in range(N + 2)]
    for i in range(1, N + 1):
        a, b = AB[i - 1]
        for t in range(T):
            dpL[i][t] = dpL[i - 1][t]
            if t >= a:
                dpL[i][t] = max(dpL[i][t], dpL[i - 1][t - a] + b)

    dpR = [[0] * (T + 1) for _ in range(N + 2)]
    for i in range(N, 0, -1):
        a, b = AB[i - 1]
        for t in range(T):
            dpR[i][t] = dpR[i + 1][t]
            if t >= a:
                dpR[i][t] = max(dpR[i][t], dpR[i + 1][t - a] + b)

    ans = 0
    for i in range(1, N + 1):
        a, b = AB[i - 1]
        for t in range(T):
            ans = max(ans, dpL[i - 1][t] + dpR[i + 1][T - 1 - t] + b)
    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, T = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    main(N, T, AB)
