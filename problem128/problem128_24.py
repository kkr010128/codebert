x, n = map(int, input().split())
lis =  []

if n == 0:
  print(x)
else:
  lis = list(map(int, input().split()))
  if x not in lis:
    print(x)
  else:
    y = x + 1
    z = x - 1
    while True:
      if y in lis and z in lis:
        y += 1
        z -= 1
      elif z not in lis:
        print(z)
        break
      elif y not in lis:
        print(y)
        break
  
