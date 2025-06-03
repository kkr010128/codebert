from math import factorial
n=int(input())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
a=0
b=0
for i in range(n-1):
  A=0
  B=0
  for j in range(i+1,n):
    if p[i]>p[j]:
      A+=1
    if q[i]>q[j]:
      B+=1
  a+=factorial(n-i-1)*A
  b+=factorial(n-i-1)*B
  
print(abs(a-b))