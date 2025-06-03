n,m=map(int,input().split())
a=[i for i in range(n+1)]
for i in list(map(int,input().split())):
    for j in range(i,n+1):
        a[j]=min(a[j-i]+1,a[j])
print(a[-1])
