n = int(input())

kuku = []
for i in range(1, 10):
    for j in range(1, 10):
        kuku.append(i * j)

if n in kuku:
    print("Yes")
else:
    print("No")
