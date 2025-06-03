import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    H, W, K = in_nn()
    a = [list(in_s()) for _ in range(H)]
    ans = [[0 for _ in range(W)] for _ in range(H)]
    stb = []

    for y in range(H):
        for x in range(W):
            if a[y][x] == '#':
                stb.append((x, y))

    for i, (x, y) in enumerate(stb):
        ans[y][x] = i + 1

    for i, (x, y) in enumerate(stb):
        l = x
        while l != 0:
            if ans[y][l - 1] == 0:
                l -= 1
            else:
                break

        r = x
        while r != W - 1:
            if ans[y][r + 1] == 0:
                r += 1
            else:
                break

        u = y
        while u != 0:
            if sum(ans[u - 1][l:r + 1]) == 0:
                u -= 1
            else:
                break

        d = y
        while d != H - 1:
            if sum(ans[d + 1][l:r + 1]) == 0:
                d += 1
            else:
                break

        for yy in range(u, d + 1):
            for xx in range(l, r + 1):
                ans[yy][xx] = i + 1

    for i in range(H):
        print(' '.join(map(str, ans[i])))


if __name__ == '__main__':
    main()
