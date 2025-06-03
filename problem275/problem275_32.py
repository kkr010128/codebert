s = 0
a = 0
for i in map(int, input().split()):
  s += max(0, (4 - i) * 100000)
  if i == 1:
    a += 1
if a == 2:
  s += 400000
print(s)