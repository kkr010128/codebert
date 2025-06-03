import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    H, W, K = map(int, input().split())
    grid = [[_ for _ in input()] for _ in range(H)]

    ans = [[0] * W for _ in range(H)]
    cnt = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '#':
                cnt += 1
                ans[h][w] = cnt

    now = -1
    for h in range(H):
        for w in range(W):
            if ans[h][w] != 0:
                now = ans[h][w]
            if ans[h][w] == 0:
                if now != -1:
                    ans[h][w] = now
        now = -1

    now = -1
    for h in range(H):
        for w in reversed(range(W)):
            if ans[h][w] != 0:
                now = ans[h][w]
            if ans[h][w] == 0:
                if now != -1:
                    ans[h][w] = now
        now = -1

    for h in range(1,H):
        if ans[h][0] == 0:
            for w in range(W):
                ans[h][w] = ans[h - 1][w]

    for h in reversed(range(H-1)):
        if ans[h][0] == 0:
            for w in range(W):
                ans[h][w] = ans[h + 1][w]

    for a in ans:
        print(*a)


resolve()