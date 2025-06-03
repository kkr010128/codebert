import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, M = map(int, readline().split())
    AC = [False] * N
    cnt = [0] * N

    for _ in range(M):
        p, s = input().split()
        p = int(p)
        p -= 1
        if s == "AC":
            AC[p] = True
        else:
            if not AC[p]:
                cnt[p] += 1

    ans_a = 0
    ans_p = 0
    for i in range(N):
        if AC[i]:
            ans_a += 1
            ans_p += cnt[i]

    print(ans_a, ans_p)


if __name__ == '__main__':
    main()
