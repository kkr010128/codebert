while True:
  a = input()
  if a == '-':
    break
  m = int(input())
  for i in range(m):
    h = int(input())
    a = a[h:]+a[:h]
  print(a)
