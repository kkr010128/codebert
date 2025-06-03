N = int(input())
As = list(map(int,input().split()))

if(N == 0):
    if(As[0] == 1):
        print(1)
    else:
        print(-1)
else:
    flag = True
    if(As[0] != 0):
        flag = False
    if(flag):
        D = [[0]*3 for i in range(N+1)]
        D[0] = [1,1,0] # mind maxD Ed
        for i in range(1,N+1):
            if(As[i] > 2*D[i-1][1]):
                flag = False
                break
            else:
                D[i][0] = max(0,D[i-1][0] - As[i])
                D[i][1] = min(2*D[i-1][1] - As[i],1 << i)
                D[i][2] = As[i]
    if(flag):
        D[N][1] = 0
        maxcnt = 0
        for i in range(N,-1,-1):
            depthmax = D[i][1] + D[i][2]
            maxcnt += depthmax
            if(i > 0):
                D[i-1][1] = min(D[i-1][1],depthmax)
        print(maxcnt)
    else:
        print(-1)
