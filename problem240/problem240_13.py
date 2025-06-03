n,m=input().split()
n=int(n)
m=int(m)
f=[0]*n
wa=[0]*n
ac=0
for i in range(m):
    p,s=input().split()
    p=int(p)-1
    if f[p]==1:
        continue
    if s=="WA":
        wa[p]+=1
    else:
        ac+=1
        f[p]=1
x=0
for i in range(n):
    if f[i]==1:
        x+=wa[i]
print(ac,x)