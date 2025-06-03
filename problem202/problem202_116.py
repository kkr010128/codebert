n, a, b = map(int, input().split())
x = n//(a+b)
y = n%(a+b)
if y > a:
  y = a
print(x*a+y)