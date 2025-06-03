import sys
from collections import deque
n,m=map(int,input().split())
s=input()
if n<=m:
    print(n)
    sys.exit()
lst=[0]*(n+1)
for i in range(1,m+1):
    if s[i]=="0":
        lst[i]=i
left=1
right=m+1
k=0
while left<n:
    if s[left]=="0":
        while right-left<=m:
            if s[right]=="0":
                lst[right]=right-left
            right+=1
            if right==n+1:
                k=n
                break
    left+=1
    if left==right or k==n:
        break
if lst[n]==0:
    print(-1)
else:
    ans=deque([])
    while k>0:
        c=lst[k]
        ans.appendleft(c)
        k-=c
    print(*ans)