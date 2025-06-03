import math
import sys
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
def euclid(a, b):
  if b == 0:
    return a
  else:
    return euclid(b, a%b)
a,b=map(int,input().split())
c=euclid(a,b)
if c==1:
  print(1)
  sys.exit()
print(len(factorization(c))+1)