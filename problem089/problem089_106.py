from collections import defaultdict


def main():
    _, _, m = map(int, input().split())

    row_dict = defaultdict(int)
    col_dict = defaultdict(int)
    row_col_dict = defaultdict(set)
    for _ in range(m):
        row, col = map(int, input().split())
        row_dict[row] += 1
        col_dict[col] += 1
        row_col_dict[row].add(col)

    max_row_val = max(row_dict.values())
    max_col_val = max(col_dict.values())

    max_rows = {k for k, v in row_dict.items() if v == max_row_val}
    max_cols = {k for k, v in col_dict.items() if v == max_col_val}
    ans = max_row_val + max_col_val - 1
    flg = False
    if ans < m:
        for row in max_rows:
            for col in max_cols:
                if not col in row_col_dict[row]:
                    ans += 1
                    flg = True
                    break
            if flg:
                break

    print(ans)


if __name__ == '__main__':
    main()
