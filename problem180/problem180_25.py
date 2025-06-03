import sys
import copy
a = [int(c) for c in input().split()]
N=a[0]
K=a[1]

#まずK*10*i<Nとなる最大のiを探す

while True:
    i = 0
    while K*10**(i+1)<N:
        i+=1
    N = abs(N-K*10**i)
    if K*10 >= N:
        break
Nmin = 10**18
while True:
    N = abs(N-K)
    if Nmin>N:
        Nmin=N
    else:
        print(Nmin)
        sys.exit(0)
