n = int(input())
s = set()
for i in range(10):
    for j in range(i, 10):
        s.add(i*j)
print('Yes' if n in s else 'No')