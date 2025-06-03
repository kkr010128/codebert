n,m=map(int,input().split())
lst=[[]for i in range(n)]
for i in range(n):
    lst[i]=list(map(int,input().split()))
lst2=[[]*1 for i in range(m)]
for i in range(m):
    lst2[i]=int(input())
for i in range(n):
    x=0
    for j in range(m):
        x=x+lst[i][j]*lst2[j]
    print("%d"%(x))

