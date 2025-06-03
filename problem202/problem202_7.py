n,a,b = map(int, input().split())
m1 = n // (a + b)
m2 = n % (a + b)

if a ==0:
  print(0)
elif a >= n:
  print(n)
elif a + b >n:
  print(a)

else:
  if m2 >= a:
    print((m1 + 1) * a )
  else:
    print(m1 * a + m2)