N, M = map(int,input().split())
ans = []

if N %2 == 0:
    L1 = list(range(1,N//2+1))
    L2 = list(range(N//2+1,N+1))
    L = len(L1)
    i = 0
    j = 0
    # print(L)
    for m in range(M):
        if m %2 == 0:
            ans.append([L1[L//2-1-i],L1[L//2+i]])
            i += 1
        else:
            ans.append([L2[L//2-1-j], L2[L//2+1+j]])
            j += 1

else:
    for i in range(1,M+1):
        ans.append([i,N+1-i])

for a in ans:
    print(*a)