n = int(input())

g = [[] for _ in range(n)]

for i in range(n):
    a = int(input())
    for j in range(a):
        x, y = map(int, input().split())
        x -= 1
        g[i].append((x, y))

ans = 0
for i in range(2**n):
    temp = [-1]*n
    for j in range(n):
        if (i >> j) & 1:
            temp[j] = 1
        else:
            temp[j] = 0
    flag = True
    for j in range(n):
        if temp[j] == 1:
            for x, y in g[j]:
                if temp[x] != y:
                    flag = False
    if flag:
        ans = max(ans, sum(temp))
print(ans)
