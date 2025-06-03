import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    H, W, M = map(int, readline().split())
    row = [0] * H
    column = [0] * W
    grid = set()

    for _ in range(M):
        h, w = map(int, readline().split())
        row[h-1] += 1
        column[w-1] += 1
        grid.add((h-1,w-1))

    max_row = max(row)
    max_column = max(column)

    idx_row = [i for i,x in enumerate(row) if x == max_row]
    idx_column = [i for i,x in enumerate(column) if x == max_column]

    ans = max_row+max_column
    flag = False

    for h in idx_row:
        for w in idx_column:
            if not (h,w) in grid:
                flag = True
                break

    if flag:
        print(ans)
    else:
        print(ans-1)


if __name__ == '__main__':
    main()
