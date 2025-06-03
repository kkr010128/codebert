import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    wn, wm, l = list(map(int, readline().split()))
    inf = 10 ** 13
    wl = [[inf] * wn for _ in range(wn)]
    for i in range(wn):
        wl[i][i] = 0

    for i in range(wm):
        wa, wb, wc = list(map(int, readline().split()))
        wl[wa - 1][wb - 1] = wc
        wl[wb - 1][wa - 1] = wc

    for i in range(wn):
        for j in range(wn):
            for k in range(wn):
                wl[j][k] = min(wl[j][k], wl[j][i] + wl[i][k])

    inf = 10 ** 13
    wwl = [[inf] * wn for _ in range(wn)]
    for i in range(wn):
        wwl[i][i] = 0

    for i in range(wn):
        for j in range(wn):
            if i != j and wl[i][j] <= l:
                wwl[i][j] = 1

    for i in range(wn):
        for j in range(wn):
            for k in range(wn):
                wwl[j][k] = min(wwl[j][k], wwl[j][i] + wwl[i][k])
    q = int(readline())
    for i in range(q):
        s, t = list(map(int, readline().split()))
        print(wwl[s-1][t-1] - 1 if wwl[s-1][t-1] != inf else -1)


if __name__ == '__main__':
    solve()
