a,b,m=map(int,input().split())
f=list(map(int,input().split()))
w=list(map(int,input().split()))
money=min(f)+min(w)
for i in range(m):
    x,y,c=map(int,input().split())
    if f[x-1]+w[y-1]-c<money:
        money=f[x-1]+w[y-1]-c
print(money)