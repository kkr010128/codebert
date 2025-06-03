n = int(input())
lst = []

for i in range(1,10):
    for j in range(1,10):
        lst.append(i*j)

print("Yes" if n in lst else "No")