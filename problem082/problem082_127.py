s, t = [input() for i in range(2)]
c = []
for i in range(len(s) - len(t) + 1):
  d = len(t)
  for a, b in zip(s[i:], t):
    if a == b:
      d -= 1
  c.append(d)
print(min(c))