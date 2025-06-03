n=int(input())
s=[]
t=[]
for i in range(9):
    s.append([])
for i in range(100):
    t.append([[],[]])
for i in range(1,n+1):
    a=str(i)
    b=max(int(a[0]),int(a[len(a)-1]))
    c=min(int(a[0]),int(a[len(a)-1]))
    if b!=0 and c!=0:
        if b==c:
            s[b-1].append(i)
        elif int(a[0])<int(a[len(a)-1]):
            t[b*9+c][0].append(i)
        else:
            t[b*9+c][1].append(i)
ans=0
for i in range(9):
    x=len(s[i])
    ans+=x**2
for i in range(100):
    x=len(t[i][0])
    y=len(t[i][1])
    ans+=2*x*y
print(ans)