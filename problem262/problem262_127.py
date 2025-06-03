N = int(input())
G = [[-1] * N for i in range(N)]
ans = 0
for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        G[i][x-1] = y
for bit in range(2**N):
    honests = []
    for i in range(N):
        if bit & (1<<i):
            honests.append(i)
    flag = True
    for j in honests:
        for k in range(N):
            if (k in honests) and G[j][k] == 0:
                flag = False
            elif(k not in honests) and G[j][k] == 1:
                flag = False
    if flag:
        ans = max(ans, len(honests))
print(ans)
