N,K=map(int,input().split())
P=list(map(int,input().split()))
X=[]
for a in P:
    X.append(a/2+0.5)
gou=sum(X[0:K])

han=-32
saigou=sum(X[N-K:N])
han=saigou
for a in range(N-K-1):

    if gou>han:
        han=gou
    gou=gou-X[a]+X[a+K]

print(han)