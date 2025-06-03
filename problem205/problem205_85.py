import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N, P = map(int, input().split())
    S = input()

    if P == 2 or P == 5:
        ans = 0
        for i in range(N):
            if int(S[i]) % P == 0:
                ans += i + 1
    else:
        val = [0] * P
        cur = 0
        tenfactor = 1
        val[cur] += 1
        for i in range(N):
            cur = (cur + int(S[N - i - 1]) * tenfactor) % P
            tenfactor *= 10
            tenfactor %= P
            val[cur] += 1

        ans = 0
        for v in val:
            ans += v * (v - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
