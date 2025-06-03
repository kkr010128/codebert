H, W, K = map(int, input().split())
cake = [input() for _ in range(H)]
# 答え
memo = [[0] * W for _ in range(H)]
#print(memo)
# 行にケーキが何個あるか
cake_count_row = [0] * H
for y in range(H):
    count = 0
    for x in range(W):
        if cake[y][x] == "#":
            count += 1
    cake_count_row[y] = count
 
# イチゴがある行について色塗り
count = 1
for y in range(H):
    first = True
    if cake_count_row[y] == 0:
        continue 
    for x in range(W):
        if cake[y][x] == "#":
            if first:
                first = False
            else:
                count += 1
        memo[y][x] = count
    count += 1

# イチゴがない行について色塗り
# 上から下に
for y in range(1, H):
    if cake_count_row[y] == 0:
        for x in range(W):
            memo[y][x] = memo[y-1][x]
# 下から上に
for y in range(H-1)[::-1]:
    if cake_count_row[y] == 0:
        for x in range(W):
            memo[y][x] = memo[y+1][x]
 
# 出力
for i in range(H):
    print(" ".join(list(map(str, memo[i]))))