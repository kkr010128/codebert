import numpy as np
n=int(input())
A=np.array(input().split(),np.int64)
A.sort()
A=A[::-1]
ans=int(0)
for i in range(n-1):
    ans+=A[(i+1)//2]
print(ans)




