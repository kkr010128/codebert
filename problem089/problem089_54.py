H, W, M = map(int, input().split())
row = [0] * (H + 1)
col = [0] * (W + 1)

bom = []
for i in range(M):
    h, w = map(int, input().split())
    bom.append([h, w])
    row[h] += 1
    col[w] += 1
 
rmax = max(row)
cmax = max(col)
cnt = row.count(rmax) * col.count(cmax)

for h, w in bom:
    if rmax == row[h] and cmax == col[w]:
        cnt -= 1

print(rmax + cmax - (cnt == 0))
