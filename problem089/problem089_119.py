import sys
input = sys.stdin.readline

h, w, m = map(int,input().split())

row = [0]*h
col = [0]*w
enemy = []

for i in range(m):
    hh, ww = map(lambda x:int(x)-1,input().split())
    row[hh] += 1
    col[ww] += 1
    enemy.append((hh,ww))

enemy = set(enemy)
rmax = max(row)
cmax = max(col)

on_r = row.count(rmax)
on_c = col.count(cmax)

on = 0
for hh, ww in enemy:
    if row[hh] == rmax and col[ww] == cmax:
        on += 1
if on == on_r*on_c:
    print(rmax+cmax-1)
else:
    print(rmax+cmax)