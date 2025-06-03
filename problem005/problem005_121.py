import math
while True:
  try:
    a,b =map(int,input().split())
    c =math.gcd(a,b)
    d =a*b// math.gcd(a,b)
    print(c,d)
  except:
    break
