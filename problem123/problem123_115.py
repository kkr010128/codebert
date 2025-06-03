from functools import reduce

n = int(input())
a = list(map(int,input().split()))
b = [0]*n
a_xor=reduce(lambda x,y : x^y,a)
for i in range(n):
  b[i]=a[i]^a_xor  
##  b[i] = reduce(lambda x,y : x^y,a[0:i+1]+a[i:])

print(" ".join(list(map(str,b))))