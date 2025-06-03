N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=list(input())
d={"r":P,"s":R,"p":S}

ans=0
for i in range(N):
    if i>=K and T[i-K]==T[i]:
            T[i]="o"
    else:
        ans+=d[T[i]]
print(ans)