H, A = map(int, input().split())

h = H//A
c = H%A

if c == 0:
  print(h)
else:
  print(h+1)