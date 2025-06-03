def gcd (x , y):
  sur = x % y
  while sur != 0:
    x = y
    y = sur
    sur = x % y
  return y

a,b = map(int,raw_input().split())
if a < b :
  temp = a
  a = b
  b = temp
print gcd(a,b)