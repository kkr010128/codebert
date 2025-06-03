N = int(input())
kuku = []
for i in range(1, 10):
  kuku += [i * j for j in range(1, 10)]
if N in kuku:
  print("Yes")
else:
  print("No")