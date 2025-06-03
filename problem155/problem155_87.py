N,M=map(int,input().split())

H=list(map(int,input().split()))

route={i:[] for i in range(1,N+1)}

for i in range(M):
    array=tuple(map(int,input().split()))
    route[array[0]].append(array[1])
    route[array[1]].append(array[0])

Obs=[True for i in range(N)]

for i in range(1,N+1):
    if Obs[i-1]==True:
        for j in route[i]:
            if H[i-1]>H[j-1]:
                Obs[j-1]=False
            else:
                Obs[i-1]=False

ans=0
for i in range(len(Obs)):
    if Obs[i]:
        ans+=1

print(ans)