def e_bomber():
    import sys
    input = sys.stdin.readline

    H, W, M = [int(i) for i in input().split()]

    bomb_row = [0] * H
    bomb_col = [0] * W
    bomb_pos = set()
    for _ in range(M):
        r, c = [int(i) - 1 for i in input().split()]
        bomb_row[r] += 1
        bomb_col[c] += 1
        bomb_pos.add((r, c))

    bomb_row_max = max(bomb_row)
    bomb_col_max = max(bomb_col)
    row_index_list = [r for r, v in enumerate(bomb_row) if v == bomb_row_max]
    col_index_list = [c for c, v in enumerate(bomb_col) if v == bomb_col_max]

    # 破壊できる数が最大になるような行と列の組を全探索する。
    # (行, 列) が破壊対象の上になってしまわないような組があれば、そこに置けばいい。
    # そのような組がまったくなければ、破壊対象の上に置かざるを得ない (-1 される)。
    for row in row_index_list:
        for col in col_index_list:
            if (row, col) not in bomb_pos:
                return bomb_row_max + bomb_col_max
    return bomb_row_max + bomb_col_max - 1

print(e_bomber())