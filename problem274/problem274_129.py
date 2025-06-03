N,M=map(int,input().split())
A,c,dp,r=[0]*N,0,0,[]
for i, s in enumerate(reversed(input())):
    if s=="1":c+=1;A[i]=c
    else:c=0
while dp+M<=N-1:
    t = M-A[dp+M]
    if t>0: dp+=t
    else:print(-1);exit()
    r.append(t)
r.append(N-dp)
print(*reversed(r))