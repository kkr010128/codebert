import sys
from collections import deque
input = sys.stdin.readline

n=int(input())
L=deque([i for i in range(1,10)])
if n<=9:
    ans = L[n-1]
else:
    cnt = 9
    for i in range(1,n):
        c=L.popleft()
        
        if c%10!=0:
            L.append(c*10+(c%10)-1)
            cnt+=1
            if cnt>=n:
                break
        L.append(c*10+(c%10))
        cnt+=1
        if cnt>=n:
            break
        
        if c%10!=9:
            L.append(c*10+(c%10)+1)
            cnt+=1
            if cnt>=n:
                break
    ans = L[-1]
print(ans)
