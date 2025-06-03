a = int(input())
b = input().split()
c = []
for i in range(a * 2):
  if i % 2 == 0:
    c.append(b[0][i // 2])
  else:
    c.append(b[1][(i - 1) // 2])
for f in c:
  print(f,end="")