from collections import deque
import itertools
def main():
    H, W = list(map(int, input().split()))
    A = [['#'] * (W + 2)] + [['#', ] + list(input()) + ['#', ] for _ in range(H)] + [['#'] * (W + 2)]
    DXY = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    ans = 0
    INF = 10000
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if A[h][w] == '#':
                continue
            count = [[-1 if i == '#' else INF for i in a] for a in A]
            count[h][w] = 0
            stack = deque([[h, w], ])
            visited = [[0] * W for _ in range(H)]
            while stack:
                x, y = stack.popleft()
                if visited[x - 1][y - 1] == 1:
                    continue
                else:
                    visited[x - 1][y - 1] = 1
                for (dx, dy) in DXY:
                    X = x + dx
                    Y = y + dy
                    if A[X][Y] == '.':
                        if visited[X - 1][Y - 1] == 0:
                            stack.append([X, Y])
                        count[X][Y] = min(count[X][Y], count[x][y] + 1)
            count = list(itertools.chain.from_iterable(count))
            ans = max(ans, max(count))
    print(ans)

if __name__ == '__main__':
    main()
