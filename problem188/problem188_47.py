x,y,a,b,c=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))
p=sorted(p,reverse=True)
q=sorted(q,reverse=True)
r=sorted(r,reverse=True)
s=[]
for i in range(x):
    s.append(p[i])
for i in range(y):
    s.append(q[i])
s=sorted(s,reverse=True)
ws=[s[0]]
for i in range(x+y-1):
    ws.append(ws[-1]+s[i+1])
wr=[r[0]]
for i in range(c-1):
    wr.append(wr[-1]+r[i+1])
ans=ws[-1]
for i in range(min(x+y-1,c)):
    ans=max(ans,ws[-2-i]+wr[i])
print(ans)

