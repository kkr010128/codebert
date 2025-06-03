n,m=map(int,input().split())

ac=[False]*n
wa=[0]*n

for i in range(m):
    p,s=input().split()
    p=int(p)-1

    if s=="AC":
        ac[p]=True
    else:
        if not ac[p]:
            wa[p]+=1

a=0
b=0

for i in range(n):
    if ac[i]:
        a+=1
        b+=wa[i]

print(a,b,sep=" ")
