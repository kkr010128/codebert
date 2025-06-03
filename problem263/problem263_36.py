import sys
import numpy as np
mod=10**9+7
n=int(sys.stdin.buffer.readline())
a=np.fromstring(sys.stdin.buffer.readline(),dtype=np.int64,sep=' ')
ans=0
b=1
for i in range(60):
    s=int((a&1).sum())
    ans=(ans+s*(n-s)*b)%mod
    a>>=1
    b=b*2%mod
print(ans)