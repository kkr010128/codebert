n,m=map(int,input().split())
a=[[0,0] for _ in range(n+1)]
x=[]
for i in range(m):
    x.append(list(input().split()))
    x[i][0]=int(x[i][0])
for i in range(m):
    if x[i][1]=="AC":
        a[x[i][0]][1]=1
    else:
        if a[x[i][0]][1]==1:
            continue
        else:
            a[x[i][0]][0]+=1
c=0
d=0
for i in range(n+1):
    c+=a[i][1]
    if a[i][1]:
        d+=a[i][0]
print(c,d)