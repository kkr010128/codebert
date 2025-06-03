a,b,c=map(int,input().split())
n = a // (b+c)
m = a - (b+c)*n
res = n*b
if m < b:
  res += m
else:
  res += b
print(res)