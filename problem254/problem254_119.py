a = int(input())
b = int(input())
d = {}
d[a] = True
d[b] = True
for i in range(1, 4):
  if i not in d:
    print(i)