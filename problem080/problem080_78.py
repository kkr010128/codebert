n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int, input().split())))

tmp1 = []
tmp2 = []
for i in range(n):
    tmp1.append([xy[i][0]+xy[i][1], xy[i][0], xy[i][1]])
    tmp2.append([xy[i][0]-xy[i][1], xy[i][0], xy[i][1]])
tmp1.sort()
tmp2.sort()

ans = 0

if (tmp1[-1][2]-tmp1[0][2])*(tmp1[-1][1]-tmp1[0][1]) >= 0:
    tmp = tmp1[-1][0]-tmp1[0][0]
    ans = max(tmp, ans)
if (tmp2[-1][2]-tmp2[0][2])*(tmp2[-1][1]-tmp2[0][1]) <= 0:
    tmp = tmp2[-1][0]-tmp2[0][0]
    ans = max(tmp, ans)

print(ans)
