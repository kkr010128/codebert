n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(n)]

ans = 12*(10**5)+1
for i in range(2**n):
    a = [0] * m
    cs = 0
    for j in range(n):
        if (i >> j) & 1:
            cs += ca[j][0]
            for k in range(1, m+1):
                a[k-1] += ca[j][k]
    flag = True
    for j in range(m):
        if a[j] < x:
            flag = False
            break
    if flag:
        ans = min(ans, cs)
if ans == 12*(10**5)+1:
    ans = -1
print(ans)