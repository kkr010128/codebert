n,k=map(int,input().split())
A=list(map(int,input().split()))
mod=10**9+7
count=k

B,C=[],[]
for i in A:
    if i<=0:B.append(i)
    else:C.append(i)
B.sort(key=lambda x:abs(x))
C.sort()

ans,flag=1,1
while k!=0:
    if k>=2:
        if len(B)>=2 and len(C)>=2:
            if B[-1]*B[-2]>C[-1]*C[-2]:
                ans *=B.pop()*B.pop()
                k -=2
            else:
                ans *=C.pop()
                k -=1
        elif len(B)>=2:
            ans *=B.pop()*B.pop()
            k -=2
        elif len(C)>=2:
            ans *=C.pop()*C.pop()
            k -=2
        else:flag=0;break
    else:
        if len(C)>0:
            ans *=C.pop()
            k -=1
        else:flag=0;break
    ans %=mod

if flag:print(ans)
else:
    ans=1
    A.sort(reverse=True)
    for i in range(count):
        ans *=A[i]
        ans %=mod
    print(ans)