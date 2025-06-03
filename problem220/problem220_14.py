r, b = input().split()

a, b = map(int, input().split())

u = input()

if r == u:
  print(a-1, b)
else:
  print(a, b-1)