n, m, x = map(int,input().split())
lst = [[0 for i in range(m + 1)]]
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(len(lst)):
        tmp2 = []
        for k in range(len(tmp)):
            y = lst[j][k] + tmp[k]
            tmp2.append(y)
        lst.append(tmp2)
ans = -1
for i in range(len(lst)):
    c = 0
    for j in range(len(lst[i])):
        if (j == 0):
            pass
        else:
            if (lst[i][j] < x):
                c = 1
    if (c == 0):
        if (ans == -1):
            ans = lst[i][0]
        else:
            ans = min(ans, lst[i][0])

print(ans)
