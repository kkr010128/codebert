n, m, x = map(int, input().split())
C = []
A = []
for i in range(n):
    temp = list(map(int, input().split()))
    c = temp[0]
    a = temp[1:]
    A.append(a)
    C.append(c)

ans = 10**18
for i in range(2**n):
    s = [0]*m
    temp = 0
    for j in range(n):
        if (i >> j) & 1:
            temp += C[j]
            for k in range(m):
                s[k] += A[j][k]
    flag = True
    for l in range(m):
        if s[l] < x:
            flag = False
    if flag:
        ans = min(ans, temp)
if ans == 10**18:
    print(-1)
else:
    print(ans)
