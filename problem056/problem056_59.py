n,m=list(map(int,input().split(' ')))
am=[[0 for j in range(m)] for i in range(n)]
bm=[0 for l in range(m)]
cm=[0 for i in range(n)]
for i in range(n):
    am[i]=list(map(int,input().split(' ')))
for j in range(m):
    bm[j]=int(input())
for i in range(n):
    for j in range(m):
        cm[i]=cm[i]+am[i][j]*bm[j]
for i in range(n):
    print(cm[i])
