A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=10**6
for i in range(M):
    x,y,z=map(int,input().split())
    m=min(a[x-1]+b[y-1]-z,m)
print(min(m,min(a)+min(b)))