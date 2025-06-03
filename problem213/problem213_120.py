N=int(input())
X=list(map(int,input().split()))
l=len(X)
s=10**10
for i in range(min(X),max(X)+1):
    x=[]
    for j in range(l):
        x.append((X[j]-i)**2)
    if s>sum(x):
        s=sum(x)
print(s)