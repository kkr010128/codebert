import numpy as np

N = int(input())
A = []
B = []
for i in range(N):
    a,b=map(int, input().split())
    A.append(a)
    B.append(b)
    
Aarray = np.array(A)
Barray = np.array(B)

medA = np.median(Aarray)
medB = np.median(Barray)

if N%2 == 1:
    ans = medB-medA+1
else:
    ans = 2*(medB-medA)+1
    

print(str(int(ans)))