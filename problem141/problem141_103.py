N=int(input())
H=list(map(int,input().split()))
depth=[0]*(N+1)
depth[0]=1
if N==0:
    if H[0]!=1:
        print(-1)
        exit()
    else:
        print(1)
        exit()
else:
    if H[0]!=0:
        print(-1)
        exit()
    for i in range(1,N+1):
        depth[i]=(depth[i-1]-H[i-1])*2
        if depth[i]<0:
            print(-1)
            exit()
    if depth[N-1]*2<H[N]:
        print(-1)
        exit()
    else:
        depth[N]=min(depth[N],H[N])
    for i in range(N - 1, -1, -1):
        if depth[i + 1] == 0:
            if H[i] != 0:
                depth[i] = H[i]
            else:
                depth[i] = 0
            if i == 0:
                depth[i] = 1
        else:
            depth[i] = min(depth[i + 1] + H[i], depth[i])
    print(sum(depth))