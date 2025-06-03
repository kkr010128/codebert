T = input()
count = 0

for c in T:
  count += 1
  if c == '?' and T[count-1] == 'D':
    c = 'P'
    print(c, end="")
  elif c == '?':
    c = 'D'
    print(c, end="")
  else:
    print(c, end="")