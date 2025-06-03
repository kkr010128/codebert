a , b , k  = map(int,input().split())
if k - a >= b:
  a = 0
  b = 0
elif k >= a and  k - a < b:
  k -= a
  a = 0
  b -= k - a
else:
  a -= k
print(a, b)
