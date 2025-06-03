INF = 10**9 + 7


def main():
    N, M, X = (int(i) for i in input().split())
    CA = [[int(i) for i in input().split()] for j in range(N)]
    ans = INF
    for bit in range(1 << N):
        wakaru = [0]*M
        cur = 0
        for i in range(N):
            if bit & (1 << i):
                c, *A = CA[i]
                cur += c
                for j in range(M):
                    wakaru[j] += A[j]
        if all(m >= X for m in wakaru):
            ans = min(ans, cur)

    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
