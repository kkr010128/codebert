#n回,m回　　X =n + 2*m  Y = 2*n + m
X,Y = map(int,input().split())
import numpy as np
from functools import reduce
import math 
a = [[1, 2], [2, 1]]
#次に逆行列を求めます。
mod = pow(10,9)+7

b = np.linalg.inv(a)


Z = np.array([[X],[Y]])

n,m=np.dot(b,Z)
p,q = *n,*m


def comb(n,k,p):
    if k==0:
        return 1
    A = reduce(lambda x,y:x*y%p ,[n-k+1+i for i in range(k)])
    B = reduce(lambda x,y:x*y%p ,[i+1 for i in range(k)])
    return A*pow(B,p-2,p)%p


if p<0 or q<0:
    print(0)
elif not abs(p-round(p))<pow(10,-3) or not abs(q-round(q))<pow(10,-3):
    print(0)
elif p==0 and q==0:
    print(0)
elif p==0:
    print(1)
elif q==0:
    print(1)
else:
    n = int(round(p))
    m = int(round(q))
    ans = comb(n+m,m,mod)

    print(ans%mod)
