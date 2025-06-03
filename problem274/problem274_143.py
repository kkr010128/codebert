import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = map(int, readline().split())
    s = input()
    t = [0] * (n + 1)

    cur = n
    for i in range(n, -1, -1):
        if s[i] == "0":
            cur = i
            t[i] = cur
        else:
            t[i] = cur

    res = []

    i = n
    while i > 0:
        nx = max(0, i - m)
        if t[nx] == i:
            return print(-1)
        else:
            res.append(i - t[nx])
            i = t[nx]

    print(*res[::-1])


if __name__ == '__main__':
    main()
