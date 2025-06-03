mod=10**9+7
n,k=map(int,input().split())
A=list(map(int,input().split()))
K=k

B,C=[],[]
for i in A:
    if i>=0:B.append(i)
    else:C.append(i)

B.sort()
C.sort(key=lambda x:abs(x))

ans,flag=1,1
while k!=0:
    if k>=2:
        point=0
        if len(B)>=2 and len(C)>=2:
            if B[-1]*B[-2]>C[-1]*C[-2]:
                ans *=B.pop()
                point=1
            else:ans *=C.pop()*C.pop()
        elif len(B)>=2:ans *=B.pop()*B.pop()
        elif len(C)>=2:ans *=C.pop()*C.pop()
        else:flag=0
        k -=2-point
    else:
        if len(B)>=1:ans *=B.pop()
        else:flag=0
        k -=1
    ans %=mod

if flag:print(ans)
else:
    ans=1
    A=sorted(A,key=lambda x:abs(x))
    for i in range(K):
        ans *=A[i]
        ans %=mod
    print(ans)