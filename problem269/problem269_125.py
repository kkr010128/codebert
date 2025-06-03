T1,T2 = list(map(int,input().split()))
A1,A2 = list(map(int,input().split()))
B1,B2 = list(map(int,input().split()))

a1 = A1*T1
a2 = A2*T2
b1 = B1*T1
b2 = B2*T2

if a1+a2 < b1+b2:
  a1,b1 = b1,a1
  a2,b2 = b2,a2
#print(a1,a2,b1,b2)

if a1+a2 == b1+b2:
  print('infinity')
else:
  if a1 > b1:
    print(0)
  else:
    c = (b1-a1)/((a1+a2)-(b1+b2))
    print(int(c)*2 if c.is_integer() else int(c)*2+1)
