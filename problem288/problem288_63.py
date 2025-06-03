import math
n= int(input())
x=n+1
for i in range(2,int(math.sqrt(n)+1)):
  if n%i==0:
    x= i+ (n/i)
print(int(x)-2)