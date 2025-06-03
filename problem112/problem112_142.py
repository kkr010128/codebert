from collections import deque
import sys
input=sys.stdin.readline

mod=10**9+7
n,k=map(int,input().split())
A=list(map(int,input().split()))
cnt=k

B,C=[],[]
for i in range(n):
    num=A[i]
    if num>=0:B.append(num)
    else:C.append(num)

B.sort(reverse=True)
C.sort()
B,C=deque(B),deque(C)

ans,flag=1,1
while k!=0:
    num=0
    length_B,length_C=len(B),len(C)
    if k>=2:
        if length_B>=2 and length_C>=2:
            plus=B[0]*B[1]
            negative=C[0]*C[1]
            if plus>negative:
                ans *=B.popleft()
                num=1
            else:ans *=C.popleft()*C.popleft()
        elif length_C>=2:ans *=C.popleft()*C.popleft()
        elif length_B>=2:ans *=B.popleft()*B.popleft()
        else:
            ans *=B.popleft()*C.popleft()
            flag=0
        k -=2-num
    else:
        if 0<length_B:ans *=B.popleft()
        elif 0<length_C:
            ans *=C.popleft()
            flag=0
        k -=1
    ans %=mod

if flag:print(ans);exit()

ans=1
A=sorted(A,key=lambda x:abs(x))
for i in range(cnt):
    ans *=A[i]
    ans %=mod
print(ans)