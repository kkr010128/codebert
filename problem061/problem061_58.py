s=input()
for c in s:
  if 'A' <= c and c <= 'Z':
    print(c.lower(), end='')
  elif 'a' <= c and c <= 'z':
    print(c.upper(), end='')
  else:
    print(c,end='')
print()
