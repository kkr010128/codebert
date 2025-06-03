n, m = map(int,input().split())
lst = [[0, 0] for i in range(n)]
for i in range(m):
    p, s = map(str,input().split())
    p = int(p) - 1
    if (lst[p][0] == 0):
        if (s == "AC"):
            lst[p][0] = 1
        else:
            lst[p][1] = lst[p][1] + 1

ans = 0
pena = 0
for i in range(n):
    if (lst[i][0] == 1):
        ans = ans + 1
        pena = pena + lst[i][1]

print(ans, pena)
