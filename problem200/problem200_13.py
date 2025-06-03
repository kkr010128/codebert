A,B,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
tmp=min(a)+min(b)
for i in range(m):
    x,y,c=map(int,input().split())
    if a[x-1]+b[y-1]-c<tmp:
        tmp=a[x-1]+b[y-1]-c
print(tmp)