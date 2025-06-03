while 1:
  s = input()
  if s == "-": break
  for _ in range(int(input())):
    h = int(input())
    s = s[h:] + s[:h]
  print(s)
