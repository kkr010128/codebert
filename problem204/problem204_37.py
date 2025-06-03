S=input()
q=int(input())
s=[]
r=[]
for i in S:
    s.append(i)
t=1
for i in range(q):
    qv=list(input().split())
    if qv[0]=='1':
        t^=1
    else:
        if int(qv[1])^t==0 or int(qv[1])^t==2:
            r.append(qv[2])
        else:
            s.append(qv[2])
            
if t==0:
    ss=s.copy()
    s=[]
    for j in range(len(ss)):
        s.append(ss[-1-j])
    ans=s
    ans.extend(r)
else:
    rr=r.copy()
    r=[]
    for j in range(len(rr)):
        r.append(rr[-1-j])
    ans=r
    ans.extend(s)
answer=''.join(ans)
print(answer)