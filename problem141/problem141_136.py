n=int(input())
A=list(map(int,input().split()))

s=0
cap=[]
flag=False
for i,a in enumerate(A):
    s*=2
    s+=a
    cap.append(min(2**i-s,(n+1-i)*10**8))
    if s>2**i:
        flag=True
        break

if flag:
    print(-1)
else:
    remain=2**n-s
    ans=0
    node=0
    for i in range(n,-1,-1):
        a=A[i]
        c=cap[i]
        node=min(c,node)+a
        ans+=node
    print(ans)
