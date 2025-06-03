n,m = map(int,input().split())
tbl=[[] for i in range(n)]
for i in range(n):
    tbl[i] = list(map(int,input().split()))
tbl2=[[]*1 for i in range(m)]
for i in range(m):
    tbl2[i] = int(input())
for k in range(n):
    x=0
    for l in range(m):
        x +=tbl[k][l]*tbl2[l]
    print("%d"%(x))
