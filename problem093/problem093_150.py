N,K = map(int, input().split())
P = [int(p) for p in input().split()]
C = [int(c) for c in input().split()]

ans = max(C)
for i in range(N):
    used = [0]*N
    used[i] = 1
    loop = [C[i]]
    j = P[i]-1
    while used[j] == 0:
        used[j] = 1
        loop.append(loop[-1]+C[j])
        j = P[j]-1
    M = len(loop)
    if K >= M:
        if K%M == 0:
            t = 0
        else:
            t = max(loop[:K%M])
            t = max(t, 0)
        num = max(loop[-1]*(K//M)+t, max(loop), loop[-1]*(K//M-1)+max(loop))
    else:
        num = max(loop[:K])
    ans = max(ans, num)
if max(C) <= 0:
    ans = max(C)
print(ans)