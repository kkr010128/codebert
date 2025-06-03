n,k=[int(i) for i in input().split()]
p=[int(i) for i in input().split()]

ex=[0]*1001
tmp=0
for i in range(1,1001):
  tmp+=i
  ex[i]=tmp/i

sumEx=[0]*(n+1)
for i in range(n):
  sumEx[i+1]=sumEx[i]+ex[p[i]]

maxA=0
for i in range(k,n+1):
  maxA=max(maxA,sumEx[i]-sumEx[i-k])
print(maxA)