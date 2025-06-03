strargs = input()

n, a, b = map(lambda x: int(x), strargs.split())

if (b - a) % 2 == 0:
  print((b - a)//2)
  
elif a - 1 < n - b:
  newB = b - a
  mid = (newB - 1)//2 + 1
  print(a + mid - 1)

else:
  newA = (a + (n - b + 1))
  mid = newA + (n - newA)//2
  print((n - b + 1) + (n - newA)//2)