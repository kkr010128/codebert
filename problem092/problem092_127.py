a,c,b = list(map(int, input().split()))

a = abs(a)
b = abs(b)
c = abs(c)

if b*c <= a:
  print(a - (b*c))
else:
  c -= a//b
  a = a%b
  #print(a,b,c)
  if c%2==0:
    print(a)
  else:
    print(abs(a-b))