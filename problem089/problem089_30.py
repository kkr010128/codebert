import sys
H,W,M = map(int,input().split())

s = [[int(item) -1 for item in input().split()] for _ in range(M)]

# print(s)

col = [0 for _ in range(H)]
row = [0 for _ in range(W)]

bomb_set = set()

# 各列と行で個数を配列
for i,j in s:
    col[i] += 1
    row[j] += 1
    bomb_set.add((i,j))    # 爆弾のある位置

# print(col)
# print(row)
# print(bomb_set)

max_col = max(col)
max_row = max(row)

# 最大の行と列を配列
max_col_index = []
max_row_index = []

# 最大の行を探す
for i in range(H):
    if col[i] == max_col:
        max_col_index.append(i)

# 最大の列を探す
for j in range(W):
    if row[j] == max_row:
        max_row_index.append(j)

# 最大の行と列の組み合わせが爆弾の位置と被っているか確認
for r in max_row_index:
    for c in max_col_index:
        if (c,r) not in bomb_set:
            ans = max_col + max_row
            print(ans)
            sys.exit()

ans = max_col + max_row -1
print(ans)