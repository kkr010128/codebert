N, M, X = map(int,input().split())
C = []
A = []
for i in range(N):
    ca = list(map(int,input().split()))
    C.append(ca[0])
    A.append(ca[1:])

INF = 10**18
ans = INF
for mask in range(1<<N):
    skill = [0 for i in range(M)]
    cost = 0
    for i in range(N):
        if mask&(1<<i):
            cost += C[i]
            for j in range(M):
                skill[j] += A[i][j]
    if min(skill) >= X:
        ans = min(ans,cost)
print(-1 if ans==INF else ans)