from fractions import gcd

def lcm(a,b):
  return a*b//gcd(a,b)

N,M = map(int,input().split())
A = [int(i) for i in input().split()]

a = 0
b = A[0]
while b % 2 == 0:
  a += 1
  b = b//2
  
for i in range(1,N):
  if A[i] % (2**a) != 0 or A[i] % (2**(a+1)) == 0:
    print(0)
    exit()

c = A[0]
for i in range(N-1):
  c = lcm(c,A[i+1])

print((M+c//2)//c)