h, w, k = map(int, input().split())
# 横に分けてから縦に切る
s = [list(input()) for _ in range(h)]
ans = 1
a = [[0]*w for _ in range(h)]
a_0 = [0]*w  # 行にイチゴがないときよう
for i in range(h):
    s_count = s[i].count("#")
    if s_count == 1:
        for j in range(w):
            a[i][j] = ans
            a_0[j] = ans
    elif s_count != 0:
        count = 0  # これは#の今現在数えた数
        for j in range(w):
            a[i][j] = ans
            a_0[j] = ans
            if s[i][j] == "#" and j+1 != w and s_count != count + 1:  # 最後のイチゴと端のイチゴの条件
                ans += 1
                count += 1
    else:
        for j in range(w):
            a[i][j] = a_0[j]

        ans -= 1
    ans += 1
for i in range(h):
    if max(a[i]) == 0:
        for j in range(h):
            if max(a[j]) != 0:
                a[i] = a[j]
                break

for i in a:
    print(*i)
