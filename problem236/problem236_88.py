div = 0
mod = 0

h = int(input())
w = int(input())
n = int(input())

if h > w:
  div = n // h
  mod = n % h
else:
  div = n // w
  mod = n % w

if mod > 0:
  print(div+1)
else:
  print(div)