N, M, X = list(map(int, input().split()))

C = [list() for _ in range(N)]
for i in range(N):
    C[i] = list(map(int, input().split()))

INF = 10**9 + 7
minpr = INF
for i in range(2**N):
    buy = list()
    for j in range(N):
        if i&1==1: buy.append(j)
        i >>= 1
    skill = [0]*M
    price = 0
    for k in range(len(buy)):
        price += C[buy[k]][0]
        for l in range(M):
            skill[l] += C[buy[k]][l+1]
    for m in range(M):
        if skill[m] < X: break
    else:
        if minpr > price: minpr = price
if minpr==INF:
    print(-1)
else:
    print(minpr)

