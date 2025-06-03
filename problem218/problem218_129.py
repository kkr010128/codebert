n=int(input())
s=[]
for i in range(n):
    s.append(input())
s.sort()
t=1
m=0
a=s[0]
for i in range(n-1):
    if s[i+1]==a:
        t+=1
    else:
        a=s[i+1]
        m=max(t,m)
        t=1
m=max(t,m)
t=1
x=[]
a=s[0]
for i in range(n-1):
    if s[i+1]==a:
        t+=1
    else:
        a=s[i+1]
        if t==m:
            x.append(s[i])
        t=1
if  t==m:
    x.append(s[len(s)-1])
for i in range(len(x)):
    print(x[i])