n=int(input())-1
radix=26
ord_a=97

ans=""
while n>=0:
  n,m=divmod(n,radix)
  ans=chr(m+ord_a)+ans
  n-=1
print(ans)