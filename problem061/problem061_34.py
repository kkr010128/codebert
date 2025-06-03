s = input()
cs = list(s)

for c in cs:
  if c.islower():
    print(c.upper(),end="")
  else :
    print(c.lower(),end="")
print()
