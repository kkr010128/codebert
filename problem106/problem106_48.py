import collections
import sys
A = []
n = int(input())
for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            A.append(i**2+j**2+k**2+i*j+j*k+k*i)
c = collections.Counter(A)


for x in range(1,n+1):
    print(c[x])
sys.exit()
