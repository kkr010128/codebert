N,K = map(int,input().split())
A = list(map(int,input().split()))
F = list(map(int,input().split()))

A = sorted(A)[::-1]
F = sorted(F)

sumA = sum(A)

if sumA <= K:
    print(0)
else:
    maxC = 0
    for i in range(N):
        tmp = A[i]*F[i]
        if maxC < tmp:
            maxC = tmp
    L = 0
    R = maxC
    visited = {}
    visited[maxC]=True
        
    while 1:
        nowC = (L+R)//2
        nowA = []
        for i in range(N):
            nowA.append(nowC//F[i])
        shugyou = 0
        for i in range(N):
            shugyou += max(A[i]-nowA[i],0)
        if shugyou <= K:
            visited[nowC] = True
            R = nowC
            if (nowC-1) in visited:
                if visited[nowC-1] == False:
                    ans = nowC
                    break
        else:
            visited[nowC] = False
            L = nowC
            if (nowC+1) in visited:
                if visited[nowC+1] == True:
                    ans = nowC+1
                    break
                
        if nowC == 0:
            if visited[nowC]==True:
                ans = 0
                break
    print(ans)