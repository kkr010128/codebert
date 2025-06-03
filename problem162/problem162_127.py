import sys

sys.setrecursionlimit(100000000)


def main():
    n, m = map(int, input().split())
    res = []
    # n = 2m+1を考える
    if m % 2 == 0:
        half_m = int(m / 2)
        for i in range(half_m):
            res.append((half_m - i, half_m + 1 + i))
            res.append((m + half_m - i, m + half_m + 2 + i))
    else:
        half_m = int(m / 2)
        for i in range(half_m):
            res.append((half_m - i, half_m + 2 + i))
            res.append((m + half_m + 1 - i, m + half_m + 2 + i))
        res.append((m + 1, m + 2 * half_m + 2))

    for r in res:
        print(str(r[0]) + " " + str(r[1]))


main()
