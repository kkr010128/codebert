import math
def fact(n):
    ans = 1
    for i in range(2, n+1):
        ans*= i
    return ans
def comb(n, c):
    return fact(n)//(fact(n-c)*c)

N,M=map(int,input().split())

if M%2==0:
  for i in range(M//2):
    print(i+1,M-i)
  for i in range(M//2):
    print(M+i+1,2*M-i+1)  
else:
  for i in range(M//2):
    print(i+1,M-i)
  for i in range(M//2+1):
    print(M+i+1,2*M-i+1)
