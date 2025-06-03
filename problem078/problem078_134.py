n=int(input())
a=10**9+7
b=10**n%a-2*9**n%a+8**n%a
if b<0:
  b+=a
print(b)