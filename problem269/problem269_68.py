t1,t2 = map(int,input().split())
a1,a2 = map(int,input().split())
b1,b2 = map(int,input().split())
a1 -= b1
a2 -= b2
if a1 < 0:
  a1 *= -1
  a2 *= -1
d = a1 * t1 + a2 * t2
if d > 0:
  print(0)
elif d == 0:
  print('infinity')
else:
  d *= -1
  l = a1 * t1
  if l % d != 0:
    print(l//d*2+1)
  else:
    print(l//d*2)
  #print(a1,a2)
  #print(d,l)