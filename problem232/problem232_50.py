a,b = map(str,input().split())

As = a * int(b)

Bs = b * int(a)

if As<Bs:
  print(As)
else:
  print(Bs)