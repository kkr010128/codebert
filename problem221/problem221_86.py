s = list(input())
count = len(s)
for i in range(count):
  s[i] = "x"
changed = "".join(s)
print(changed)