n,a,b = map(int,input().split())
if a == 0:
  print(0)
elif a+b <= n and n%(a+b) < a:
  print((n//(a+b))*a + n%(a+b))
elif a+b <= n and n%(a+b) >= a:
  print((n//(a+b))*a + a)
elif n < a+b and n < a:
  print(n)
elif n < a+b and a <= n:
  print(a)
  
