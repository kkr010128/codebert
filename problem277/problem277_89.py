import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, K = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(H)]

    cnt = 0
    res = [[0] * W for _ in range(H)]
    for h in range(H):
        num = 0
        for w in range(W):
            if grid[h][w] == "#":
                cnt += 1
                num = cnt
            res[h][w] = num

    for h in range(H):
        num = 0
        for w in reversed(range(W)):
            if res[h][w]:
                num = res[h][w]
            res[h][w] = num

    for w in range(W):
        for h in range(1, H):
            if res[h][w] == 0:
                res[h][w] = res[h - 1][w]

    for w in range(W):
        for h in reversed(range(H)):
            if res[h][w] == 0:
                res[h][w] = res[h + 1][w]

    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
