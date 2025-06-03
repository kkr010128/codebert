k = int(input())
l = str(input())

if k >= len(l):
  print(l)
else:
  print(l[:k]+"...")