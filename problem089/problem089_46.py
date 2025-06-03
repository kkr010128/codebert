H, W, M = map(int, input().split())

bomb = set()
row = [0] * H
column = [0] * W

for i in range(M):
    h, w = map(int, input().split())
    h -= 1
    w -= 1
    
    bomb.add((h, w))
    
    row[h] += 1
    column[w] += 1
    
row_max = max(row)
col_max = max(column)

r_check = []
c_check = []
for i in range(H):
    if row[i] == row_max:
        r_check.append(i)

for i in range(W):
    if column[i] == col_max:
        c_check.append(i)

num = len(r_check) * len(c_check)

ans = row_max + col_max - 1
flg = False
if M < num:
    ans += 1
else:
    for r in r_check:
        if flg:
            break
        for c in c_check:
            if not (r, c) in bomb:
                ans += 1
                flg = True
                break

print(ans)