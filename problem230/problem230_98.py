n,d,a = map(int,input().split())
xh = [list(map(int,input().split())) for _ in range(n)]
xh.sort()

ans = 0
att = [0]*n
cnt = 0
f = []
f1 = [0]*n

for x,h in xh:
    f.append(h)

for i in range(n):
    tmp = xh[i][0] + 2 * d
    while cnt < n:
        if xh[cnt][0] <= tmp:
            cnt += 1
        else:
            break
    att[i] = min(cnt-1, n-1)

for i in range(n):
    if f[i] > 0:
        da = -(-f[i]//a)
        ans += da
        f1[i] -= da * a
        if att[i]+1 < n:
            f1[att[i]+1] += da * a
    if i < n-1:
        f1[i+1] += f1[i]
        f[i+1] += f1[i+1]
print(ans)
