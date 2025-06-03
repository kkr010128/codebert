import numpy as np
n=int(input())
d_i = list(map(int, input().split()))  
d=np.array(d_i)
out=0
for i in range(1,n):
    a=d_i.pop(0)
    d_i.append(a)
    out+=np.dot(d,np.array(d_i))
print(int(out/2))