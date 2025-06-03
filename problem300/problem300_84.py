import math

A,B = map(int,input().split())
G = math.gcd(A,B)

N = G
#素因数分解
sep = []
for i in range(2,int(math.sqrt(N))+2,1):
    if N % i ==0:
        count = 0
        while N % i == 0:
            N = N//i
            count += 1
        sep.append([i,count])
if N != 1:
    sep.append([N,1])

print(len(sep)+1)