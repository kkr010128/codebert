import numpy as np

def solve():
    ret = np.array([[1 for _ in range(W)] for _ in range(H)])
    row_groups = np.array([0 for _ in range(H)])
    row_group_set = set()
    prev_row = 0
    for row in range(H):
        if '#' in s[row]:
            row_groups[prev_row: row + 1] = row
            row_group_set.add(row)
            prev_row = row + 1
    row_groups[prev_row: ] = prev_row - 1

    cur_group_num = 1
    for row in row_group_set:
        prev_col = 0
        for col in range(W):
            if s[row][col] == '#':
                ret[row][prev_col: col + 1] = cur_group_num
                cur_group_num += 1
                prev_col = col + 1
            ret[row][prev_col: ] = cur_group_num - 1

    for row, row_group_num in enumerate(row_groups):
        if row in row_group_set:
            continue
        for col in range(W):
            ret[row][col] = ret[row_group_num][col]

    for row in ret:
        print(' '.join(map(str, row.tolist())))

if __name__ == "__main__":
    H, W, K = map(int, input().split())
    s = []
    for row in range(H):
        s.append(list(input()))
    solve()