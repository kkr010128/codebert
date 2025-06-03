N=int(input())

if N==1:
    print("a")
    exit()

from collections import deque
from collections import Counter
abc="abcdefghijklmnopqrstuvwxyz"
ans=["a"]

for i in range(1,N):
    d=deque(ans)
    ans=[]
    while d:
        temp=d.popleft()
        temp2=list(temp)
        cnt=Counter(temp2)
        L=len(cnt)
        for j in range(L+1):
            ans.append(temp+abc[j])

for a in ans:
    print(a)





