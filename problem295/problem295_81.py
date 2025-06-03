import sys


def solve():
    input = sys.stdin.readline
    mod = 10 ** 9 + 7
    wn, wm, wwl = list(map(int, input().rstrip('\n').split()))
    inf = 10 ** 13
    wl = [[inf] * wn for _ in range(wn)]
    for i in range(wn):
        wl[i][i] = 0

    for i in range(wm):
        wa, wb, wc = list(map(int, input().rstrip('\n').split()))
        wl[wa - 1][wb - 1] = wc
        wl[wb - 1][wa - 1] = wc

    for i in range(wn):
        for j in range(wn):
            for k in range(wn):
                wl[j][k] = min(wl[j][k], wl[j][i] + wl[i][k])

    nwl = [[inf] * wn for _ in range(wn)]
    for i in range(wn):
        for j in range(wn):
            if wl[i][j] <= wwl:
                nwl[i][j] = 1

    for i in range(wn):
        for j in range(wn):
            for k in range(wn):
                nwl[j][k] = min(nwl[j][k], nwl[j][i] + nwl[i][k])

    q = int(input().rstrip('\n'))
    for i in range(q):
        s, t = list(map(int, input().rstrip('\n').split()))
        print(nwl[s-1][t-1] - 1 if nwl[s-1][t-1] != inf else -1)


if __name__ == '__main__':
    solve()
