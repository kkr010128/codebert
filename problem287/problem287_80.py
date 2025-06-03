N = int(input())
kuku = []
for i in range(1, 10):
  for j in range(1, 10):
    kuku.append(i * j)
print("Yes" if N in kuku else "No")