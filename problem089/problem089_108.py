h,w,m = map(int,input().split())
hw = [list(map(int,input().split())) for i in range(m)]
hb = [0] * h
wb = [0] * w

for i in range(m):
    hb[hw[i][0]-1] += 1
    wb[hw[i][1]-1] += 1

max_h = max(hb)
max_w = max(wb)
ans = max_h + max_w
count = hb.count(max_h) * wb.count(max_w)
for i in range(m):
    if hb[hw[i][0]-1] == max_h and wb[hw[i][1]-1] == max_w:
        count -= 1
if count <= 0:
    ans -= 1
print(ans)