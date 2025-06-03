while True:
  s = input()
  if s == '-':
    break
  for n in range(int(input())):
    h = int(input())
    s = s[h:]+s[:h]
  print(s)