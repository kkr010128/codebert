H, W, K = map(int, input().split())

ans = [[0 for _ in range(W)] for _ in range(H)]
not_ichigo_row = []
ichigo_row = []

cnt = 0 #イチゴのカウント、フラグが立っていない場合はカウントしない
for i in range(H):
    s = list(input())
    # print(s)
    if "#" not in s:
        not_ichigo_row.append(i)
        continue

    ichigo_row.append(i)
    f = 0 #行内の1つめのイチゴか判定
    cnt += 1
    for j in range(W):
        # print(s[j])
        if s[j] == "#":
            if not f:
                f = 1
            else:
                cnt += 1
        # print("cnt", cnt)
        ans[i][j] = cnt

# print(not_ichigo_row)
for i in not_ichigo_row:
    row = i
    f = 0
    while row in not_ichigo_row:
        if row == H-1:
            f = 1
        if f:
            row -= 1
        else:
            row += 1
    # print(row)
    ans[i] = ans[row].copy()

for r in ans:
    print(*r)
