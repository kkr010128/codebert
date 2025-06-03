n,m=map(int,input().split())
p,s=[],[]
for i in range(m):
    a,b=map(str,input().split())
    p.append(int(a))
    s.append(b)
c,e=0,0
l=[0]*n
for i in range(m):
    if s[i]=="WA" and l[p[i]-1]==0:
        e+=1
    elif s[i]=="AC" and l[p[i]-1]==0:
        c+=1
        l[p[i]-1]=1
for i in range(m):
    if s[i]=="WA" and l[p[i]-1]==0:
        e-=1
print(str(c)+" "+str(e))