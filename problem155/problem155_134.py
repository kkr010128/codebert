N,M = map(int,input().split())
H = list(map(int,input().split()))
AB = [tuple(map(int,input().split())) for i in range(M)]
ans=0
es = [[] for _ in range(N)]
for a,b in AB:
    a,b = a-1,b-1
    es[a].append(b)
    es[b].append(a)
for i in range(N):
    for j in es[i]:
        if H[j]>=H[i]:
            break
    else:
        ans+=1


print(ans)