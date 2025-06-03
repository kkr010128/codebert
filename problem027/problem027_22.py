import sys, os, math, bisect, itertools, collections, heapq, queue

# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def koch(N, ax, ay, bx, by):
    if N == 0: return

    # 度をラジアンに変換
    radians = math.radians(60)
    # 線分を3等分する、
    # 座標sと座標tの位置を求める
    sx = (2 * ax + bx) / 3
    sy = (2 * ay + by) / 3
    tx = (ax + 2 * bx) / 3
    ty = (ay + 2 * by) / 3

    # 座標sと座標tから正三角形となる座標uを求める
    ux = (tx - sx) * math.cos(radians) - (ty - sy) * math.sin(radians) + sx
    uy = (tx - sx) * math.sin(radians) + (ty - sy) * math.cos(radians) + sy

    # 座標aと座標sのコッホ曲線を求める
    koch(N - 1, ax, ay, sx, sy)
    print('{:.08f} {:.08f}'.format(sx, sy))  # 座標s

    # 座標sと座標uのコッホ曲線を求める
    koch(N - 1, sx, sy, ux, uy)
    print('{:.08f} {:.08f}'.format(ux, uy))  # 座標u

    # 座標uと座標tのコッホ曲線を求める
    koch(N - 1, ux, uy, tx, ty)
    print('{:.08f} {:.08f}'.format(tx, ty))  # 座標t

    # 座標tと座標bのコッホ曲線を求める
    koch(N - 1, tx, ty, bx, by)


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    print('{:.08f} {:.08f}'.format(0, 0))  # 座標a
    koch(N, 0, 0, 100, 0)
    print('{:.08f} {:.08f}'.format(100, 0))  # 座標b


if __name__ == '__main__':
    main()

