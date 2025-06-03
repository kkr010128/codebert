h, w, k = map(int, input().split())
s = [list(input()) for _ in range(h)]
# 2次元累積和
acum = [[0]*(w+1) for _ in range(h+1)]
for i in range(h):
    for j in range(w):
        acum[i+1][j+1] = acum[i][j+1] + acum[i+1][j] - acum[i][j] + int(s[i][j])
#print(acum)


def white_choco_count(x1, y1, x2, y2):
    return acum[y2][x2] - acum[y2][x1] - acum[y1][x2] + acum[y1][x1]


ans = float("inf")
for rows in range(2**(h-1)):
    count = 0
    hlist = []
    for i in range(h-1):
        if rows >> i & 1 == 1:
            count += 1  # 横線の数カウントしておく
            hlist.append(i+1)
    hlist.append(h)
    #print(hlist)
    x1 = 0
    for x2 in range(w):
        y1 = 0
        for y2 in hlist:
            if white_choco_count(x1, y1, x2, y2) > k:
                count += float("inf")
            # kを超えてはいけないが、一個右で縦に割るとｋを超える必要がある（貪欲にやるので）
            elif white_choco_count(x1, y1, x2, y2) <= k < white_choco_count(x1, y1, x2+1, y2):
                count += 1
                # 次のブロックにいくのでx1更新(ただしy1の更新はx2がｗまでおわったあとにしたいのでbreak使うとうまくいく）
                x1 = x2
                break
            y1 = y2
    # ここまでで、x2=0, 1, ..., w-1 までみたが、x2 = wのとき（ブロックの右端）を見てない
    y1 = 0
    for y2 in hlist:
        if white_choco_count(x1, y1, w, y2) > k:
            count += float("inf")
        y1 = y2
    #print(count)
    ans = min(ans, count)
print(ans)

