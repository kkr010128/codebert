n,m=map(int,input().split())
l=[[0,0] for i in range(n)]
for i in range(m):
    p,s=input().split()
    p=int(p)
    if s=="AC":
        if l[p-1][0]!=1:
            l[p-1][0]=1
    else:
        if l[p-1][0]!=1:
            l[p-1][1]+=1
ac=0
wa=0
for i in range(len(l)):
    ac+=l[i][0]
    if l[i][0]!=0:
        wa+=l[i][1]
print(ac,wa)