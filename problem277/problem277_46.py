h, w, k = map(int, input().split())
tizu = [list(input()) for _ in range(h)]
ans = [[0 for _ in range(w)] for _ in range(h)]
pos = 0
bef = 0
bef_flg = True
for i in range(h):
    pos_tmp = pos
    f_st = False
    if "#" in tizu[i]:
        bef_flg = False
        pos += 1
        for j in range(w):
            if tizu[i][j] == "#":
                if f_st:
                    pos += 1
                f_st = True
            ans[i][j] = pos
    else:
        if bef_flg:
            bef += 1
        else:
            for j in range(w):
                ans[i][j] = ans[i - 1][j]

for i in range(bef - 1, -1, -1):
    for j in range(w):
        ans[i][j] = ans[i + 1][j]
for row in ans:
    print(*row)

