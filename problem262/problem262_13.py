n = int(input())
XY = []
for i in range(n):
    a = int(input())
    xy = []
    for j in range(a):
        x, y = map(int, input().split())
        xy.append([x, y])
    XY.append(xy)
ans = 0
for i in range(2 ** n):
    s = [0] * n
    cnt = 0
    case = True
    for j in range(n):
        if (i >> j) & 1:
            s[j] = 1
            cnt += 1
    for k in range(n):
        if s[k] == 1:
            for l in range(len(XY[k])):
                if s[XY[k][l][0] - 1] != XY[k][l][1]:
                    case = False
    if case is True:
        ans = max(ans, cnt)
print(ans)
