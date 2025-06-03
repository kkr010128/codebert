import numpy as np

        
n = int(input())

a = np.zeros(n,dtype=int)
b = np.zeros(n,dtype=int)

for i in range(n):
    a[i],b[i] = map(float, input().split())

#listをsortする
a.sort()
b.sort()
                    
if n%2 == 1:
    a0cen = a[(n-1)//2]
    b0cen = b[(n-1)//2]
    nn = b0cen - a0cen + 1
else:
    a0cen1 = a[(n-2)//2]+a[n//2]
    b0cen1 = b[(n-2)//2]+b[n//2]
    nn = int(b0cen1 -a0cen1 +1)

print(nn)           
